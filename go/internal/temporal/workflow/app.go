package workflow

const TaskQueueName = "AI-message"
const PythonTaskQueueName = "AI-message-python"
const WorkflowIdPrefix = "ai-message-"

type MessageData struct {
	Text string
}

type ResponseMessageData struct {
	Response string
}
