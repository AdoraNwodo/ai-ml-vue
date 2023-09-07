import * as pulumi from "@pulumi/pulumi";
import * as vercel from "@pulumiverse/vercel";

// A project that is connected to a git repository.
// Deployments will be created automatically
// on every branch push and merges onto the Production Branch.
const withGit = new vercel.Project("withGit", {
    framework: "vuejs",
    gitRepository: {
        repo: "adoranwodo/ai-ml-vue",
        type: "github",
    },
});
// A project that is not connected to a git repository.
// Deployments will need to be created manually through
// terraform, or via the vercel CLI.
const example = new vercel.Project("example", {framework: "vuejs"});