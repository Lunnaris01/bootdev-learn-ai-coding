import { Plugin } from "@opencode/plugin";

declare const Bun: any;

export default Plugin.define({
  id: "run-slop",
  setup: async (ctx) => {
    await ctx.tool.transform((tools) => {
      tools.add({
        name: "run_slop",
        description: "Run a .slop program with the Sloperator interpreter and return stdout, stderr and exit code",
        input: {
          type: "object",
          properties: {
            path: {
              type: "string",
              description: "Path to the .slop file, relative to the project root or absolute",
            },
          },
          required: ["path"],
          additionalProperties: false,
        },
        options: { codemode: false },
        output: {
          type: "object",
          properties: {
            stdout: { type: "string" },
            stderr: { type: "string" },
            exitCode: { type: "number" },
          },
          required: ["stdout", "stderr", "exitCode"],
          additionalProperties: false,
        },
        execute: async (input) => {
          const { path } = input as { path: string };
          const projectRoot =
            ctx.location.project.directory ?? ctx.location.directory;

          const proc = Bun.spawnSync(
            ["uv", "run", "--no-active", "sloperator.py", path],
            { cwd: projectRoot },
          );

          const stdout = proc.stdout.toString();
          const stderr = proc.stderr.toString();
          const exitCode = proc.exitCode ?? 1;

          return {
            output: { stdout, stderr, exitCode },
            content: JSON.stringify({ stdout, stderr, exitCode }),
          };
        },
      });
    });
  },
});
