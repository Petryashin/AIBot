package main

import (
	"context"
	"log"
	"os"
	"sync"

	"github.com/Petryashin/AIBot/internal/temporal/workflow"
	"go.temporal.io/sdk/client"
)

func main() {
	c, err := client.Dial(client.Options{})
	if err != nil {
		return
	}

	options := client.StartWorkflowOptions{
		ID:        workflow.WorkflowIdPrefix + os.Args[1],
		TaskQueue: workflow.TaskQueueName,
	}

	req := workflow.MessageData{
		Text: os.Args[2],
	}

	we, err := c.ExecuteWorkflow(
		context.Background(),
		options,
		workflow.SendMessageWorkflow,
		req)

	if err != nil {
		log.Fatalf("Failed to execute workflow: %v", err)
	}

	var wg sync.WaitGroup
	wg.Add(1)

	go func() {
		defer c.Close()
		defer wg.Done()
		var result workflow.ResponseMessageData

		err := we.Get(context.Background(), &result)

		if err != nil {
			log.Println("Failed to get workflow result:", err)
			return
		}

		log.Println("Workflow completed. ResponseMessage:" + result.Response)
	}()

	wg.Wait()
}
