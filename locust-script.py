from locust import HttpUser, task, between, events
import json

class QuickstartUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        files = ['hash_recurse', 'recursive_calls', 'storage_read_writes', 'storage_writes']
        self.request_bodies = {}
        for file_name in files:
            with open(f'request_files/{file_name}.json') as f:
                self.request_bodies[file_name] = json.load(f)
                
    @task
    def test_hash_recursive(self):
        if self.request_bodies:
            file_name = 'hash_recurse'
            request_body = self.request_bodies[file_name]                
            with self.client.post("/", json=request_body, headers={'Content-Type': 'application/json'}, catch_response=True, name=file_name) as response:
                if response.status_code == 200:
                    if 'error' in response.json():
                        response.failure(f"Request failed with status code {response.status_code}")
                    else:
                        response.success()
                else:
                    response.failure(f"Request failed with status code {response.status_code}")
    
    @task
    def test_recursive_calls(self):
        if self.request_bodies:
            file_name = 'recursive_calls'
            request_body = self.request_bodies[file_name]                
            with self.client.post("/", json=request_body, headers={'Content-Type': 'application/json'}, catch_response=True, name=file_name) as response:
                if response.status_code == 200:
                    if 'error' in response.json():
                        response.failure(f"Request failed with status code {response.status_code}")
                    else:
                        response.success()
                else:
                    response.failure(f"Request failed with status code {response.status_code}")              

    @task
    def test_storage_read_writes(self):
        if self.request_bodies:
            file_name = 'storage_read_writes'
            request_body = self.request_bodies[file_name]                
            with self.client.post("/", json=request_body, headers={'Content-Type': 'application/json'}, catch_response=True, name=file_name) as response:
                if response.status_code == 200:
                    if 'error' in response.json():
                        response.failure(f"Request failed with status code {response.status_code}")
                    else:
                        response.success()
                else:
                    response.failure(f"Request failed with status code {response.status_code}")

    @task
    def test_storage_writes(self):
        if self.request_bodies:
            file_name = 'storage_writes'
            request_body = self.request_bodies[file_name]                
            with self.client.post("/", json=request_body, headers={'Content-Type': 'application/json'}, catch_response=True, name=file_name) as response:
                if response.status_code == 200:
                    if 'error' in response.json():
                        response.failure(f"Request failed with status code {response.status_code}")
                    else:
                        response.success()
                else:
                    response.failure(f"Request failed with status code {response.status_code}")