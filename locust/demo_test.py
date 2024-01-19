from locust import HttpUser, task

class User(HttpUser): 
    @task 
    def get_echo(self) -> None:
        self.client.get("/nginxbackend-clusterip-timeout")