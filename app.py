from fastapi import FastAPI

app = FastAPI()

import hashlib 

text = "hello world"
hash_object = hashlib.sha256(text.encode())
hash_digest = hash_object.hexdigest()
print("SHA Hash of", text , "is ", hash_digest)

@app.get("/")
def root():
    def hash_file(file_path):
        h = hashlib.new("sha256")
        with open(file_path, "rb") as file: 
            while True:
                chunk = file.read(1024)
                if chunk == b"": 
                    break 
                h.update(chunk)
        return h.hexdigest()
