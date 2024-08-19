import boto3
import csv


def main():
    dynamodb = boto3.resource(
        "dynamodb",
        endpoint_url="http://localhost:8181",
        region_name="ap-northeast-1",
        aws_access_key_id="AKI000000000000000",
        aws_secret_access_key="secret_access_key",
    )
    table = dynamodb.Table("witches")

    csv_file = open("./resources/witches.csv", "r", encoding="utf-8")
    csv_reader = csv.reader(csv_file)
    with table.batch_writer() as batch:
        for i, row in enumerate(csv_reader):
            if i == 0:
                continue

            batch.put_item(
                Item={
                    "id": i,
                    "name": row[0],
                    "nation": row[1],
                    "branch": row[2],
                    "unit": row[3],
                    "team": row[4],
                    "birthday": row[5],
                    "image": row[6],
                }
            )


main()
