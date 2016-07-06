from twitter import post_tweet


def tweet_closed_task(task):
    tweet = "Finalizei a tarefa no TaskManager: " + task
    post_tweet(tweet)


def tweet_closed_project(project):
    tweet = "Finalizei o projeto no TaskManager: " + project
    post_tweet(tweet)
