from celery import Celery

# Define the Celery instance and specify RabbitMQ as the broker
celery_app = Celery(
    "worker", 
    broker="amqp://guest:guest@localhost//",  # RabbitMQ URL (default: guest:guest)
    backend="rpc://",  # Optional backend for task results (RPC is often used with RabbitMQ)
)

# Example task
@celery_app.task
def add(x, y):
    return x + y
