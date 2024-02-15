from promptflow import PFClient

if __name__ == "__main__":
    client = PFClient()

    # _ = client.run(flow="main", data="main/data.jsonl", stream=True)
    _ = client.run(flow="eval", data="eval/data.jsonl", stream=True)
