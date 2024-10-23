package workflow

import (
	"time"

	"go.temporal.io/sdk/temporal"
	"go.temporal.io/sdk/workflow"
)

func SendMessageWorkflow(ctx workflow.Context, data MessageData) (ResponseMessageData, error) {
	var response ResponseMessageData
	logger := workflow.GetLogger(ctx)

	retryPolicy := &temporal.RetryPolicy{
		InitialInterval:    15 * time.Second,
		BackoffCoefficient: 2.0,
		MaximumInterval:    time.Second * 60,
		MaximumAttempts:    10,
	}

	options := workflow.ActivityOptions{
		StartToCloseTimeout: time.Second * 30,
		RetryPolicy:         retryPolicy,
		TaskQueue:           PythonTaskQueueName,
	}

	ctx = workflow.WithActivityOptions(ctx, options)

	// Python activity call
	err := workflow.ExecuteActivity(ctx, "GetAIAnswer", data).Get(ctx, &response)
	if err != nil {
		return response, err
	}

	logger.Info("Python activity result: ", response.Response)

	return response, nil
}
