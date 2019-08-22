def publish_messages(project_id, topic_name,data):
	"""Publishes multiple messages to a Pub/Sub topic."""
	# [START pubsub_quickstart_publisher]
	# [START pubsub_publish]
	from google.cloud import pubsub_v1
	data = str(data)
	publisher = pubsub_v1.PublisherClient()
	# The `topic_path` method creates a fully qualified identifier
	# in the form `projects/{project_id}/topics/{topic_name}`
	topic_path = publisher.topic_path(project_id, topic_name)
	print(topic_path)
	# Data must be a bytestring
	print("data :" + data)
	data = data.encode('utf-8')
	# When you publish a message, the client returns a future.
	future = publisher.publish(topic_path, data=data)
	print(future.result())
	print('Published messages.')
