[![OpenStax](https://img.shields.io/badge/OpenStax-Data-00A6C9?style=for-the-badge&logo=openstax&logoColor=white)](https://openstax.org)
# OpenStax Data Lambda Template (Python)

The project source includes function code and supporting resources:

- `function` - A Python function.
- `template.yml` - An AWS CloudFormation template that creates an application.
- `1-create-bucket.sh`, `2-build-layer.sh`, etc. - Shell scripts that use the AWS CLI to deploy and manage the application.

Use the following instructions to deploy the sample application.

# Requirements
- [Python 3.7](https://www.python.org/downloads/). Sample also works with Python 3.8 and 3.9. 
- The Bash shell. For Linux and macOS, this is included by default. In Windows 10, you can install the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to get a Windows-integrated version of Ubuntu and Bash.
- [The AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) v1.17 or newer.

# Setup
Download or clone this repository.

    $ git clone https://github.com/openstax/data-lambda-template.git

Make a copy of the directory and change to the new directory.

    $ cp -r data-lambda-template project-name-lambda
    $ cd project-name-lambda

Update the following files with your project name and function code:\
_changes required are in `<change me>` format_

- `template.yml`
- `deploy.sh`
- `invoke.sh`
- `cleanup.sh`
- `function/lambda_function.py` (where you write the code)
- `function/requirements.txt` (where you list the dependencies)
- `function/tests/test_lambda_function.py` (where you write the tests)

To create a new bucket for deployment artifacts, run `1-create-bucket.sh`.

    $ ./1-create-bucket.sh
    make_bucket: lambda-artifacts-a5e491dbb5b22e0d

To build a Lambda layer that contains the function's runtime dependencies, run `2-build-layer.sh`. Packaging dependencies in a layer reduces the size of the deployment package that you upload when you modify your code.

    $ ./2-build-layer.sh

# Deploy
To deploy the application, run `3-deploy.sh`.

    $ ./3-deploy.sh
    Uploading to e678bc216e6a0d510d661ca9ae2fd941  9519118 / 9519118.0  (100.00%)
    Successfully packaged artifacts and wrote output template to file out.yml.
    Waiting for changeset to be created..
    Waiting for stack create/update to complete
    Successfully created/updated stack - data-lambda-template

This script uses AWS CloudFormation to deploy the Lambda functions and an IAM role. If the AWS CloudFormation stack that contains the resources already exists, the script updates it with any changes to the template or function code.

# Test
To invoke the function, run `4-invoke.sh`.

    $ ./4-invoke.sh
    {
        "StatusCode": 200,
        "ExecutedVersion": "$LATEST"
    }
    {"TotalCodeSize": 410713698, "FunctionCount": 45}

Let the script invoke the function a few times and then press `CRTL+C` to exit.

The application uses AWS X-Ray to trace requests. Open the [X-Ray console](https://console.aws.amazon.com/xray/home#/service-map) to view the service map. The following service map shows the function calling Amazon S3.


Choose a node in the main function graph. Then choose **View traces** to see a list of traces. Choose any trace to view a timeline that breaks down the work done by the function.

# Cleanup
To delete the application, run `5-cleanup.sh`.

    $ ./5-cleanup.sh
