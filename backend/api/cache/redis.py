from redis import Redis

r = Redis(host="cache",
          port=6379,
          username="default",
          password="mypassword",
          db=0)
