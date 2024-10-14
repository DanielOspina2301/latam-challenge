from fastapi import FastAPI, HTTPException
from google.cloud import bigquery

from src.queries.queries import top_dates_query

app = FastAPI()

# Initialize bigquery client
client = bigquery.Client.from_service_account_json(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))


@app.get("/top_dates")
async def query_top_dates():

    try:
        # Execute query
        query_job = client.query(top_dates_query)

        # Get results
        results = query_job.result()  # Espera a que la consulta se complete

        # Convert to list
        data = [dict(row) for row in results]

        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)