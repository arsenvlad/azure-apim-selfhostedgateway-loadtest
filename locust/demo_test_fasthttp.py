from locust import task, FastHttpUser

class User(FastHttpUser): 
    @task 
    def get_echo(self):
        self.client.get("/nginxbackend-clusterip")
