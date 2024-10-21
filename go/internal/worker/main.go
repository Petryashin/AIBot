package main

import (
	"log"

	"github.com/Petryashin/AIBot/internal/temporal/workflow"
	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/worker"
)

func main() {
	c, err := client.Dial(client.Options{})
	if err != nil {
		log.Fatalln("Failed to create Temporal client", err)
	}
	defer c.Close()

	w := worker.New(c, workflow.TaskQueueName, worker.Options{})

	w.RegisterWorkflow(workflow.SendMessageWorkflow)
	err = w.Run(worker.InterruptCh())
	if err != nil {
		log.Fatalln("Unable to start worker", err)
	}
}
