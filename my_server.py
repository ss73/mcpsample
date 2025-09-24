from fastmcp import FastMCP

from call_agent import AgentCaller

mcp = FastMCP(
    name="CoArchitect MCP Server",
    instructions="""
        A multi-capability agent that helps with software architecture tasks, including:
        - Generating RFCs (Request for Comments) documents
        - Performing threat modeling
        - Analyzing documents for best practices
        The agent has access to various documents relating to architecture within Securitas
        Digital and SDP (Secure Digital Platform), such as architectural decision records,
        system documentation and guiding principles.
        """
    )

@mcp.tool
def analyze_document(document: str) -> str:
    """
    Analyze the provided document and return recommendations to align with best practices.
    """
    print("Analyzing document...")
    agent_caller = AgentCaller(
        endpoint="https://coarch-resource.services.ai.azure.com/api/projects/coarch",
        agent_id="asst_WCW9rE22OnLr4FgCOhqOekRy"
    )
    return agent_caller.ask(f"Analyze the following document and provide recommendations: {document}")


@mcp.tool
def create_rfc(synopsis: str) -> str:
    """
    Create an RFC (Request for Comments) document in Markdown format using the standard template.
    """
    print(f"Creating RFC document...")
    agent_caller = AgentCaller(
        endpoint="https://coarch-resource.services.ai.azure.com/api/projects/coarch",
        agent_id="asst_WCW9rE22OnLr4FgCOhqOekRy"
    )
    return agent_caller.ask(f"Given the synopsis below, create markdown (md) output for an RFC using the standard RFC template. Apply best practices found in ADRs and available system documentation.\n\nSynopsis:\n\n {synopsis}")

@mcp.resource("resource://rfc_template")
def rfc_template() -> str:
    """
    Provides a template for writing RFCs.
    """
    return """
    # RFC Template

    ## Title

    ## Abstract

    ## Justification

    ## Specification

    ## Backwards Compatibility

    ## Security Considerations

    ## References
    """

@mcp.prompt
def threat_modeling_prompt() -> str:
    """
    Generates a user message for threat modeling.
    """
    print("Generating threat modeling prompt...")
    return "Provide a threat model section for the application. You should include potential threats and mitigation strategies. Follow the STRIDE model and use markdown (md) formatting."

if __name__ == "__main__":
    mcp.run()