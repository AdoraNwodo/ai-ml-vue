"""A Python Pulumi program"""

import pulumi
import pulumiverse_vercel as vercel

# Load config settings from `pulumi config set` user commands
config = pulumi.Config()
backendDns = config.require("backendDns")
token = config.require_secret("token")
repoName = config.require("repoName")
repoType = config.require("repoType")

provider = vercel.Provider("vercel-provider",
    api_token = token
)

project = vercel.Project("vercel-project", 
    name = "vercel-git-project",
    framework = "vue",
    git_repository = vercel.ProjectGitRepositoryArgs(
        repo = repoName,
        type = repoType
    ),
    root_directory = "./src/app/katwalk-frontend",
    opts = pulumi.ResourceOptions(
        provider = provider
    )
)

environment = vercel.ProjectEnvironmentVariable("vercel-env",
    project_id = project.id,
    key = "VUE_APP_BACKEND_DNS",
    value = backendDns,
    targets = ["production"],
    opts = pulumi.ResourceOptions(
        provider = provider
    )
)

deployment = vercel.Deployment("vercel-deployment",
    project_id = project.id,
    production = True,
    ref = "main",
    opts = pulumi.ResourceOptions(
        provider = provider
    )
)