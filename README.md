# MCPify REST APIs

Transform REST APIs into AI agent tools using Amazon Bedrock AgentCore Gateway - complete tutorial with EKS deployment and MCP integration.

## 🎯 What You'll Build

This repository contains a complete end-to-end tutorial for "MCPifying" REST APIs - transforming them into Model Context Protocol (MCP) tools that AI agents can use naturally through conversational interfaces.

- **Sample REST API** - A retail API with products, orders, and customer management
- **EKS Deployment** - Complete Kubernetes deployment with HTTPS and load balancing
- **AgentCore Gateway** - Transform REST endpoints into MCP tools
- **AI Agent Integration** - Connect to QuickSuite and other AI platforms

## 📚 Complete Tutorial

The main tutorial is available in the `agentcore-integration/` directory:

**[📖 MCPifying Applications with AgentCore Gateway](agentcore-integration/MCPifying_Applications_with_AgentCore_Gateway.md)**

This comprehensive guide covers:
- Setting up HTTPS with ACM certificates
- Deploying applications on EKS
- Creating AgentCore Gateway with OAuth authentication
- Testing MCP tools with AI agents
- End-to-end integration examples

## 🏗️ Repository Structure

```
├── agentcore-integration/     # Main tutorial and AgentCore Gateway setup
│   ├── MCPifying_Applications_with_AgentCore_Gateway.md
│   ├── deploy_retail_gateway_boto3.py
│   └── test_deployed_gateway.py
├── app/                       # Sample retail API application
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── k8s/                       # Kubernetes deployment manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── namespace.yaml
├── terraform/                 # Infrastructure as Code
│   ├── main.tf
│   ├── variables.tf
│   └── terraform.tfvars.example
├── scripts/                   # Deployment and testing scripts
│   ├── build-and-push.sh
│   └── deploy.sh
└── screenshots/               # Tutorial screenshots and examples
```

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/aidinkhosrowshahi/mcpify-rest-apis.git
   cd mcpify-rest-apis
   ```

2. **Follow the main tutorial**
   Open `agentcore-integration/MCPifying_Applications_with_AgentCore_Gateway.md` and follow the step-by-step guide.

3. **Configure your environment**
   - Update `terraform/terraform.tfvars` with your AWS account details
   - Replace placeholder values in configuration files
   - Set up your domain and certificates

## 🔧 Prerequisites

- AWS Account with appropriate permissions
- AWS CLI configured
- kubectl installed and configured
- Docker installed
- Terraform (optional, for infrastructure setup)
- Python 3.8+ (for AgentCore Gateway deployment)

## 🎯 Key Features

- **Complete Tutorial**: Step-by-step guide from REST API to MCP tools
- **Production Ready**: HTTPS, authentication, and security best practices
- **Scalable Architecture**: EKS deployment with load balancing
- **AI Agent Integration**: Works with QuickSuite, Claude, and other AI platforms
- **Sanitized Examples**: All sensitive information replaced with placeholders

## 📖 What is MCPification?

MCPification is the process of transforming traditional REST APIs into Model Context Protocol (MCP) tools that AI agents can discover, understand, and use autonomously. Instead of requiring developers to write custom integrations, MCPified APIs become immediately available to AI agents through natural language interfaces.

**Before MCPification:**
```bash
curl -X POST https://api.example.com/orders \
  -H "Content-Type: application/json" \
  -d '{"customer_id": 123, "items": [...]}'
```

**After MCPification:**
```
User: "Create an order for customer 123 with 2 laptops and 1 mouse"
AI Agent: *automatically calls the create_order MCP tool*
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Amazon Bedrock AgentCore team for the gateway technology
- Model Context Protocol specification contributors
- AWS EKS and container services teams

---

**Ready to MCPify your APIs?** Start with the [complete tutorial](agentcore-integration/MCPifying_Applications_with_AgentCore_Gateway.md)! 🚀