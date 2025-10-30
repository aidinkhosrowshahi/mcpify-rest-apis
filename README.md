# MCPifying Your Existing Applications: From REST APIs to AI Agent Tools with Amazon AgentCore Gateway

*Transform your EKS applications into intelligent agent tools using Amazon Bedrock AgentCore Gateway and the Model Context Protocol (MCP)*

---

## Introduction: The Agent Revolution is Here

Imagine your existing REST API suddenly becoming a set of intelligent tools that AI agents can discover, understand, and use autonomously. No more writing custom integrations for every agent framework. No more maintaining separate tool definitions. Just one gateway that transforms your application into a universal agent toolkit.

This is the power of "MCPifying" your applications with Amazon Bedrock AgentCore Gateway.

In this deep dive, we'll walk through transforming a real-world retail application running on Amazon EKS into a set of MCP (Model Context Protocol) tools that Amazon QuickSuite can use. We'll build the complete architecture: **Amazon QuickSuite → AgentCore Gateway → EKS Application**, covering every component from Cognito authentication to natural language interactions, showing you exactly how to bridge the gap between traditional applications and the agent-driven future.

## Understanding the Key Technologies

Before we dive into MCPifying applications, let's understand the key technologies that make this transformation possible.

### What is the Model Context Protocol (MCP)?

**MCP** is an open standard that lets AI agents discover and use tools automatically. Think of it as a universal language - any MCP-compatible agent can use any MCP server without custom integration code.

### What is Amazon Bedrock AgentCore?

**Amazon Bedrock AgentCore** enables you to deploy and operate highly effective agents securely, at scale using any framework and model. With AgentCore, developers can accelerate AI agents into production with the scale, reliability, and security critical to real-world deployment. AgentCore provides tools and capabilities to make agents more effective and capable, purpose-built infrastructure to securely scale agents, and controls to operate trustworthy agents. AgentCore services are composable and work with popular open-source frameworks and any model, so you don't have to choose between open-source flexibility and enterprise-grade security and reliability.

**AgentCore Gateway** *(Our Focus)*
Amazon Bedrock AgentCore Gateway provides an easy and secure way for developers to build, deploy, discover, and connect to tools at scale. AI agents need tools to perform real-world tasks—from querying databases to sending messages to analyzing documents. With Gateway, developers can convert APIs, Lambda functions, and existing services into Model Context Protocol (MCP)-compatible tools and make them available to agents through Gateway endpoints with just a few lines of code. Gateway supports OpenAPI, Smithy, and Lambda as input types, and is the only solution that provides both comprehensive ingress authentication and egress authentication in a fully-managed service. Gateway also provides 1-click integration with several popular tools such as Salesforce, Slack, Jira, Asana, and Zendesk. Gateway eliminates weeks of custom code development, infrastructure provisioning, and security implementation so developers can focus on building innovative agent applications.

**📖 Learn More:** For additional insights on accelerating development with AgentCore, see the AWS blog post: [Accelerate development with the Amazon Bedrock AgentCore MCP Server](https://aws.amazon.com/blogs/machine-learning/accelerate-development-with-the-amazon-bedrock-agentcore-mcpserver/).

### What is Amazon QuickSuite?

**Amazon QuickSuite** is a comprehensive, generative AI-powered business intelligence platform that makes it easy to analyze data, create visualizations, automate workflows, and collaborate across your organization. The service combines traditional business intelligence capabilities with modern AI assistance, requiring no machine learning expertise to use. You can connect to diverse data sources, create interactive dashboards, build intelligent automations, and get immediate insights through natural language conversations with AI agents.

**QuickSuite Chat Agents** help users explore data, analyze information, and take actions through natural language conversations. Chat agents can evolve from simple question-answering interfaces to advanced functions that orchestrate complex workflows using connected tools - like your MCPified retail API.

**Perfect for MCPification:**
- **Built-in MCP Support**: Native integration with MCP servers like AgentCore Gateway
- **Natural Language Interface**: Ask "Show me all orders" and get data + visualizations
- **No ML Expertise Required**: Business users can interact with complex systems easily
- **Workflow Automation**: Build intelligent automations using your MCPified tools

## What Does "MCPifying" Actually Mean?

**MCPifying** is the process of transforming existing applications and APIs into Model Context Protocol (MCP) compatible tools. Instead of your API being just a collection of endpoints, it becomes a discoverable, self-describing toolkit that AI agents can understand and use intelligently.

Here's what happens when you MCPify an application:

**Before MCPifying:**
```
User → Custom Integration → EKS Application
```

**After MCPifying (Our Demo Architecture):**
```
User → Amazon QuickSuite → AgentCore Gateway → EKS Application
```

![AgentCore EKS Architecture](agentcore-eks.jpg)

The magic is in that middle layer - AgentCore Gateway acts as a universal translator that:
- Converts your OpenAPI specification into MCP tool definitions
- Handles authentication and authorization
- Provides semantic search for tool discovery
- Manages rate limiting and error handling
- Offers a standardized interface for any agent framework

### The Complete Flow

**Business User** → **QuickSuite** → **AgentCore Gateway** → **Your EKS Application**

QuickSuite connects to AgentCore Gateway via MCP protocol, which translates requests to your existing REST API. Your application doesn't need to change - it just gains AI superpowers!

## Getting Started with the Demo Repository

*Note: This section shows you how to deploy a complete demo environment. If you already have an existing application running on EKS or any other platform, you can skip directly to the MCPification process and adapt the concepts to your existing setup.*

**🎯 Demo Repository:**
All the code, deployment scripts, and configuration files for this blog post are available in this repository structure:

```bash
# Repository structure
mcpify-retail-demo/
├── app/                    # Flask retail application
├── k8s/                    # Kubernetes manifests
├── terraform/              # EKS infrastructure
├── scripts/                # Build and deployment scripts
└── agentcore-integration/  # AgentCore Gateway deployment
```

**🚀 Quick Start (Assuming EKS Already Exists):**

⚠️ **First**: Update placeholder values in configuration files (see Configuration Checklist below)

```bash
# 1. Build and deploy the retail application
./scripts/build-and-push.sh us-east-1 retail-api
./scripts/deploy.sh retail-demo-eks us-east-1

# 2. Deploy AgentCore Gateway
cd agentcore-integration
python deploy_retail_gateway_boto3.py --api-url https://YOUR_ACTUAL_DOMAIN

# 3. Test the complete integration
python test_deployed_gateway.py retail_gateway_config_boto3_*.json
```

**🏗️ Complete Setup (Including EKS):**
If you need to create the EKS cluster first, follow the detailed deployment steps below.

The repository includes:
- **Complete Flask application** with AgentCore Gateway compatibility
- **Kubernetes deployment manifests** for EKS
- **Terraform infrastructure** for EKS cluster setup
- **AgentCore Gateway deployment scripts** using boto3
- **Testing and validation scripts**

## Complete Deployment Guide

This section provides step-by-step instructions for deploying the complete demo environment. If you used the Quick Start above and already have everything running, you can skip to the MCPification process.

**🚨 Prerequisites:**
- **Custom Domain Name**: You need a domain name (e.g., `api.yourcompany.com`)
- **AWS Account**: With permissions to create ACM certificates and Route 53 records
- **Domain Control**: Ability to validate domain ownership via DNS

**🔧 Configuration Checklist:**

Before starting deployment, you'll need to replace placeholder values in these files:

1. **`terraform/terraform.tfvars`:**
   - `domain_name = "api.yourcompany.com"` → Your actual domain

2. **`k8s/ingress.yaml`:**
   - `YOUR_ACCOUNT_ID` → Your AWS account ID
   - `YOUR_REGION` → Your AWS region (e.g., `us-east-1`)
   - `YOUR_CERTIFICATE_ID` → Your ACM certificate ID
   - `YOUR_DOMAIN` → Your actual domain

3. **`k8s/deployment.yaml`:**
   - `YOUR_ACCOUNT_ID` → Your AWS account ID

4. **Gateway deployment command:**
   - `https://api.yourcompany.com` → Your actual domain

**💡 Tip:** Use find-and-replace in your editor to update all placeholders consistently.

### Step 1: HTTPS Setup

AgentCore Gateway requires HTTPS endpoints. Set up your domain and SSL certificate first:

**1. Create ACM Certificate:**
```bash
# Request a certificate for your domain
aws acm request-certificate \
  --domain-name api.yourcompany.com \
  --validation-method DNS \
  --region YOUR_REGION
```

**2. Configure Route 53 (Recommended):**
```bash
# Create a hosted zone for your domain
aws route53 create-hosted-zone \
  --name api.yourcompany.com \
  --caller-reference $(date +%s)
```

**3. Validate the Certificate:**
- Go to AWS Certificate Manager console
- Find your certificate and add the CNAME record to your DNS
- Wait for validation to complete (5-10 minutes)

**4. Update Terraform Configuration:**
```hcl
# terraform/terraform.tfvars
domain_name = "api.yourcompany.com"  # Your actual domain
```

### Step 2: EKS Cluster Setup

**Create an EKS cluster using the included Terraform configuration:**

```bash
# Navigate to terraform directory
cd terraform

# Configure your settings
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your AWS region and domain:
# - aws_region = "us-east-1"  # Your preferred region
# - domain_name = "api.yourcompany.com"  # Your actual domain

# Create the complete EKS infrastructure
terraform init
terraform plan
terraform apply

# Update your kubeconfig
aws eks update-kubeconfig --region YOUR_REGION --name retail-demo-eks
```

**The Terraform configuration creates:**
- **VPC with public/private subnets** across 3 availability zones
- **EKS cluster** with managed node groups (t3.medium instances)
- **Security groups** with proper ingress/egress rules
- **IAM roles** for cluster and node groups
- **AWS Load Balancer Controller** for ingress support

### Step 3: Deploy the Retail Application

**Prerequisites:**
- EKS cluster running with AWS Load Balancer Controller installed
- kubectl configured
- Docker image built and pushed to ECR

**⚠️ Important**: Complete the HTTPS setup process above before proceeding.

**Build and Push Docker Image:**

Use the provided script to build and push the Docker image to ECR:

```bash
# Build and push Docker image (creates ECR repository if needed)
./scripts/build-and-push.sh us-east-1 retail-api

# The script automatically:
# - Builds the Docker image from the app/ directory
# - Creates ECR repository if it doesn't exist
# - Logs into ECR
# - Tags and pushes the image
# - Outputs the image URI for deployment
```

**Deploy the Application:**

The repository includes pre-configured Kubernetes manifests (namespace, deployment, service, ingress) with HTTPS support. The ingress is configured to:
- Redirect HTTP traffic to HTTPS automatically
- Use your ACM certificate for SSL termination
- Route traffic to the retail API pods

**🔧 Important Configuration Updates:**

Before deploying, update the Kubernetes manifests with your actual values:

1. **Update `k8s/ingress.yaml`:**
   - Replace `YOUR_ACCOUNT_ID` with your AWS account ID
   - Replace `YOUR_REGION` with your AWS region
   - Replace `YOUR_CERTIFICATE_ID` with your ACM certificate ID
   - Replace `YOUR_DOMAIN` with your actual domain

2. **Update `k8s/deployment.yaml`:**
   - Replace `YOUR_ACCOUNT_ID` with your AWS account ID

**Deploy to EKS:**

Use the provided deployment script:

```bash
# Deploy the retail API to EKS (installs ALB controller if needed)
./scripts/deploy.sh retail-demo-eks us-east-1

# The script automatically:
# - Updates kubeconfig for the specified cluster
# - Installs AWS Load Balancer Controller
# - Applies all Kubernetes manifests from k8s/
# - Waits for deployment to be ready
# - Shows the ALB endpoint

# Check deployment status manually if needed
kubectl get deployments -n retail-demo
kubectl get pods -n retail-demo
kubectl get ingress -n retail-demo
```

**Configure DNS (Final Step):**

After deployment, point your domain to the ALB endpoint:

```bash
# Get the ALB endpoint
ALB_ENDPOINT=$(kubectl get ingress retail-api-ingress -n retail-demo -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
echo "ALB Endpoint: $ALB_ENDPOINT"

# Option 1: Route 53 (if you set up Route 53 in the HTTPS Setup Guide)
aws route53 change-resource-record-sets \
  --hosted-zone-id YOUR_HOSTED_ZONE_ID \
  --change-batch '{
    "Changes": [{
      "Action": "CREATE",
      "ResourceRecordSet": {
        "Name": "api.yourcompany.com",
        "Type": "CNAME",
        "TTL": 300,
        "ResourceRecords": [{"Value": "'$ALB_ENDPOINT'"}]
      }
    }]
  }'

# Option 2: Other DNS providers - Create a CNAME record:
# Name: api.yourcompany.com
# Type: CNAME  
# Value: [ALB_ENDPOINT from above]

# Wait for DNS propagation (5-15 minutes)
nslookup api.yourcompany.com
```

### Step 4: Test Your Demo Application

Once deployed, test your endpoints using the actual deployed URL:

```bash
# Replace with your actual deployed application URL
API_URL="https://YOUR_DOMAIN"

# Test health check
curl $API_URL/health

# Test orders
curl $API_URL/orders

# Test products
curl $API_URL/products

# Test specific product
curl $API_URL/product/prod_001

# Test creating an order
curl -X POST $API_URL/order \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "cust_001",
    "items": [
      {"product_id": "prod_001", "name": "Laptop", "quantity": 1, "price": 999.99}
    ]
  }'

# Test analytics
curl $API_URL/analytics/sales

# Test inventory
curl $API_URL/inventory
```

**Expected Response Examples:**

```json
// GET /health
{
  "status": "healthy",
  "timestamp": "2024-01-29T15:30:45.123456"
}

// GET /orders
{
  "orders": [
    {
      "id": "ord_001",
      "customer_id": "cust_001",
      "items": [
        {"product_id": "prod_001", "name": "Laptop", "quantity": 1, "price": 999.99}
      ],
      "total": 1059.97,
      "status": "completed",
      "created_at": "2024-01-15T10:30:00Z"
    }
  ],
  "count": 2
}
```

Now that we have our demo application running, let's proceed to MCPify it!

## Step 5: Deploy AgentCore Gateway

Now that your EKS cluster is running and the retail application is deployed and tested, let's MCPify it by deploying the AgentCore Gateway.

### Prerequisites for Gateway Deployment:
- ✅ HTTPS setup completed (Step 1)
- ✅ EKS cluster is running (Step 2)
- ✅ Retail application is deployed and accessible via HTTPS (Steps 3-4)
- ✅ AWS CLI configured with AgentCore permissions

**Verify HTTPS is Working:**
```bash
# This should work without SSL errors (replace with your actual domain)
curl https://YOUR_ACTUAL_DOMAIN/health
```

### Deploy the AgentCore Gateway:

```bash
# Navigate to the agentcore-integration directory
cd agentcore-integration

# Deploy AgentCore Gateway with your actual API URL
python deploy_retail_gateway_boto3.py --api-url https://YOUR_ACTUAL_DOMAIN

# The script automatically handles:
# - IAM service role creation with proper trust policies
# - Cognito User Pool and OAuth configuration
# - AgentCore Gateway creation with MCP protocol
# - OpenAPI target setup with your application endpoints
# - Configuration file generation for integration

# Test the deployed gateway
python test_deployed_gateway.py retail_gateway_config_boto3_*.json
```

**🔗 Important: Update Your API URL**

**🔧 Configuration Requirements:**
- Replace `https://YOUR_ACTUAL_DOMAIN` with your actual domain from Step 1
- Ensure this matches the domain you configured in `k8s/ingress.yaml` and `terraform/terraform.tfvars`
- The script automatically updates the OpenAPI specification with your URL
- This ensures AgentCore Gateway connects to your deployed EKS application

### What the Deployment Script Creates

The `deploy_retail_gateway_boto3.py` script creates a complete AgentCore Gateway infrastructure with the following components:

#### **1. IAM Service Role (`RetailGatewayServiceRole`)**
Creates an IAM role with trust policies that allows AgentCore Gateway to securely access AWS services and manage gateway operations with proper logging permissions.

#### **2. Amazon Cognito User Pool & OAuth Configuration**
Creates a complete OAuth 2.0 authentication system with User Pool, domain, resource server, and app client to enable secure machine-to-machine authentication for QuickSuite integration.

#### **3. AgentCore Gateway**
Creates a fully managed MCP-compatible gateway service with OAuth JWT authorization and semantic search capabilities that transforms your REST API into discoverable MCP tools.

#### **4. API Key Credential Provider**
Creates a credential provider that handles API key authentication in HTTP headers, ensuring secure access patterns even for demo/public APIs.

#### **5. OpenAPI Target**
Creates the target configuration that links your retail API to the gateway. The script dynamically generates a complete OpenAPI specification with your actual API URL and all 12 retail endpoints, then converts each endpoint into MCP tool definitions that agents can discover and use.

#### **6. Configuration File (`retail_gateway_config_boto3_*.json`)**
Generates a complete configuration file with OAuth credentials, gateway URLs, and all connection details needed for QuickSuite integration and testing.

**Result:** Your retail API is now MCPified and ready for AI agent integration!

## Step 5.1: Gather Configuration Details

Before configuring QuickSuite, you need to collect the connection details from your deployed AgentCore Gateway.

### Find Your Gateway Configuration

The deployment script created a configuration file with all the details you need. Look for a file named `retail_gateway_config_boto3_*.json` in the `agentcore-integration` directory.

**📋 Required Information for QuickSuite:**

1. **MCP Server Endpoint**: 
   - Found in config file as `gateway_url`
   - Format: `https://YOUR_GATEWAY_ID.gateway.bedrock-agentcore.YOUR_REGION.amazonaws.com/mcp`

2. **Client ID**: 
   - Found in config file as `client_id`
   - Example: `52raa9kv7jqopghs4n38s1duqv`

3. **Client Secret**: 
   - Found in config file as `client_secret`
   - Example: `nl2caoljennp28bpis7g3j3s7ft0rkdpa3390m8egmfps86rtkq`

4. **Token URL**: 
   - Found in config file as `token_endpoint`
   - Format: `https://YOUR_COGNITO_DOMAIN.auth.YOUR_REGION.amazoncognito.com/oauth2/token`

### View Your Configuration File

```bash
# Navigate to agentcore-integration directory
cd agentcore-integration

# List the generated config files
ls retail_gateway_config_boto3_*.json

# View the configuration (replace with your actual filename)
cat retail_gateway_config_boto3_*.json
```

**Example Configuration File:**
```json
{
  "gateway_url": "https://retail-demo-boto3-abc123-xyz789.gateway.bedrock-agentcore.us-east-1.amazonaws.com/mcp",
  "gateway_id": "retail-demo-boto3-abc123-xyz789",
  "client_id": "52raa9kv7jqopghs4n38s1duqv",
  "client_secret": "nl2caoljennp28bpis7g3j3s7ft0rkdpa3390m8egmfps86rtkq",
  "token_endpoint": "https://retail-demo-boto3-abc123-domain-abc123.auth.us-east-1.amazoncognito.com/oauth2/token",
  "scope": "retail-demo-boto3-abc123/genesis-gateway:invoke",
  "region": "us-east-1"
}
```

**💡 Keep this information handy** - you'll need it in the next step to configure QuickSuite.

### Alternative: Find Values in AWS Console

If you can't find the config file, you can also retrieve these values from the AWS Console:

**MCP Server Endpoint:**
1. Go to Amazon Bedrock console → AgentCore → Gateways
2. Find your gateway (name starts with `retail-demo-boto3-`)
3. Copy the Gateway URL and add `/mcp` at the end

**OAuth Credentials:**
1. Go to Amazon Cognito console → User pools
2. Find your user pool (name starts with `retail-demo-boto3-`)
3. Go to "App integration" → "App clients and analytics"
4. Find your app client to get the Client ID and Client Secret
5. Go to "App integration" → "Domain" to construct the Token URL

## Step 6: Configure QuickSuite Integration

With your AgentCore Gateway deployed and configuration details ready, let's connect it to Amazon QuickSuite for natural language interactions.

### Configure QuickSuite MCP Integration

**1. Access MCP Settings in QuickSuite**

Navigate to the MCP configuration section in QuickSuite to add your AgentCore Gateway as an MCP server. Look for the "Integrations" section in your QuickSuite under connections.

<img src="screenshots/qs-mcp-01.png" alt="QuickSuite MCP Settings - Access the MCP configuration section to manage server connections" width="800"/>

**2. Add New MCP Server Configuration**

Click "Model Context Protocol" to begin configuring your AgentCore Gateway connection. This opens the MCP server configuration form where you'll define the connection parameters.

<img src="screenshots/qs-mcp-02.png" alt="Add MCP Server Configuration - Configure your AgentCore Gateway connection settings" width="800"/>

Configure these essential settings using values from your config file:
- **Name**: `Retail Demo Gateway` (or any name you prefer)
- **Description**: `MCPified retail API for order and product management`
- **MCP server endpoint**: Copy the `gateway_url` value from your config file
  - Example: `https://retail-demo-boto3-abc123-xyz789.gateway.bedrock-agentcore.us-east-1.amazonaws.com/mcp`

**3. Configure OAuth 2.0 Authentication**

Set up the OAuth credentials using the values from your gateway configuration file from Step 5.1.

<img src="screenshots/qs-mcp-03.png" alt="OAuth Configuration - Set up OAuth 2.0 client credentials for secure authentication" width="800"/>

**Authentication Settings Configuration:**

1. **Authentication Method**: Select **Service authentication**
2. **Authentication Type**: The system will automatically detect OAuth 2.0 client credentials
3. **Required OAuth 2.0 Fields** (copy from your config file):
   - **Client ID**: Copy the `client_id` value from your config file
   - **Client Secret**: Copy the `client_secret` value from your config file  
   - **Token URL**: Copy the `token_endpoint` value from your config file

**💡 Tip**: Keep your config file open in a text editor to easily copy these values.

**4. Test Connection and Discover Tools**

QuickSuite will automatically test the OAuth connection and discover all available MCP tools from your AgentCore Gateway.

<img src="screenshots/qs-mcp-04.png" alt="Connection Test and Tool Discovery - Verify successful connection and view discovered MCP tools" width="800"/>

**5. Integration Complete**

Your MCP integration is now fully configured and ready for use. You should see all your retail API tools available.

<img src="screenshots/qs-mcp-07.png" alt="MCP Integration Complete - Connection active and ready for use" width="800"/>

## Step 7: Test the Complete Integration

Now you can interact with your retail application through natural language:

**Example Business Intelligence Interactions:**

*Business User*: "Show me all the orders"
*QuickSuite*: *Uses MCP client to call `listOrders` tool via AgentCore Gateway*
*Response*: Displays an interactive dashboard with order data and insights

*Business User*: "What's our current inventory situation?"
*QuickSuite*: *Calls `getInventory` tool through MCP*
*Response*: Creates a comprehensive inventory dashboard with stock levels and alerts

*Business User*: "Create an order for our top customer"
*QuickSuite*: *Calls multiple tools: `listCustomers`, then `createOrder`*
*Response*: Creates order and updates dashboards in real-time

## Congratulations! Your Application is Now MCPified

You've successfully transformed your retail application from a traditional REST API into an intelligent agent toolkit.



**Your API Tools:**
Your retail endpoints (`/health`, `/orders`, `/products`, etc.) are now MCP tools (`checkHealth`, `listOrders`, `listProducts`, etc.) that AI agents can discover, understand, and use in natural language conversations.

![AgentCore EKS Architecture](agentcore-eks.jpg)





## Troubleshooting Common Issues

### Issue 1: OAuth Token Failures

**Symptoms**: 401 Unauthorized errors
**Solutions**:
- Verify client ID and secret
- Check token endpoint URL
- Ensure scope matches resource server configuration
- Validate Cognito domain is active

### Issue 2: Tool Discovery Problems

**Symptoms**: Empty tool list or missing tools
**Solutions**:
- Validate OpenAPI specification syntax
- **Ensure OpenAPI spec uses HTTPS URLs** (required by AgentCore Gateway)
- **Verify API key authentication is defined** in OpenAPI spec security section
- Check gateway target status
- Verify IAM role permissions
- Review CloudWatch logs for parsing errors

### Issue 3: Tool Call Failures

**Symptoms**: Tools discovered but calls fail
**Solutions**:
- Test underlying API directly
- Check credential provider configuration
- Validate request/response schemas
- Review gateway exception logs

## Conclusion

We've transformed a traditional REST API into an AI-native toolkit using **Amazon QuickSuite → AgentCore Gateway → EKS Application**. 

**Key Takeaways:**
- MCPification creates discoverable, self-describing tools for AI agents
- Your existing APIs can become agent tools without code changes  
- HTTPS and proper authentication are essential
- OpenAPI documentation becomes the foundation for agent tools

Your existing applications contain functionality that agents can leverage. With AgentCore Gateway, you can unlock that potential without rewriting application code.

The agent revolution is here - it's time to MCPify your applications.

---

*Ready to MCPify your applications? Use the automated deployment script provided in this guide to get started quickly. The future of application integration is agent-native, and it starts with your first MCPified API.*

## How This Solution Was Built and Published

This complete MCPification solution was built using **[Kiro IDE](https://kiro.dev/)** - an AI-powered development environment that accelerated the creation of this multi-service application from concept to working demo in hours.

**Kiro IDE enabled:**
- Rapid prototyping and automated code generation
- Seamless coordination of Flask app, Kubernetes, Terraform, and AgentCore Gateway
- End-to-end testing and comprehensive documentation

**Use Kiro IDE for your MCPification projects:**
- Clone this repository and explore it in Kiro IDE
- Build your own MCPified applications with AI assistance
- Generate deployment scripts and infrastructure code automatically

**Ready to build your own MCPified applications?** Try **[Kiro IDE](https://kiro.dev/)** for AI-accelerated development.

## Enhancing Code Generation with MCP Tools

Your MCPified applications can enhance your development workflow by providing live context to LLMs for code generation.

**Add AgentCore MCP Server to Kiro IDE or other development tools:**
```json
{
  "mcpServers": {
    "bedrock-agentcore-mcp-server": {
      "command": "uvx",
      "args": [
        "awslabs.amazon-bedrock-agentcore-mcp-server@latest"
      ],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": [
        "search_agentcore_docs",
        "fetch_agentcore_doc"
      ]
    }
  }
}
```



**Benefits:**
- **AgentCore expertise**: Kiro can access official AgentCore documentation and best practices
- **Context-aware code generation**: LLMs query live APIs for accurate data structures
- **Implementation guidance**: Get help with AgentCore Gateway integration using official docs
- **Auto-documentation**: Generate API docs and SDKs from live endpoints

**Integrate with:** Kiro IDE, Cursor IDE, GitHub Copilot, Claude Desktop, or custom LLM tools.

This creates a powerful feedback loop where your MCPified applications and official AgentCore knowledge enhance your development capabilities!

## 🎓 A Quick Note

**This is a learning demo!** We built this to show you how MCPification works, but please don't drop it straight into production. Take time to understand the code, add proper security, and test everything thoroughly in your environment. You know your systems best - make sure everything fits your needs and standards!