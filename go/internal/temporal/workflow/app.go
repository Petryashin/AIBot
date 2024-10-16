package workflow

const TaskQueueName = "AI-message"
const WorkflowIdPrefix = "ai-message-"

type MessageData struct {
	Text string
}

type ResponseMessageData struct {
	Response string
}
