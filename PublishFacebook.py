import datetime
import facebook
import aiohttp
import aiosqlite


async def read_rows():
    conn = await aiosqlite.connect('socialdesktop.db')
    cursor = await conn.cursor()
    current_timestamp = datetime.datetime.now()
    query = "SELECT * FROM facebook WHERE timestamp < ?"
    await cursor.execute(query, (current_timestamp,))
    rows = await cursor.fetchall()

    access_token = 'dd'
    page_id = ''

    async with aiohttp.ClientSession() as session:
        graph = facebook.GraphAPI(access_token, session)
        for row in rows:
            try:
                _, msg, image_bytes = row
                photo_id = await graph.put_photo(image_bytes, album_path=page_id + "/photos", message=msg)['post_id']
                
                # save posts to history table (Possible Future Feature)

            except facebook.GraphAPIError as e:
                print(f"An error occurred: {e.message}")

    await cursor.close()
    await conn.close()