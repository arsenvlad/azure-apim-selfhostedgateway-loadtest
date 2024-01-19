from locust import HttpUser, task

class User(HttpUser): 
    @task 
    def get_echo(self) -> None:
        with self.client.get("/nginxbackend-clusterip", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            elif response.elapsed.total_seconds() > 60:
                response.failure("Request took too long" + str(response.elapsed.total_seconds()))
            else:
                response.failure("Something else went wrong")