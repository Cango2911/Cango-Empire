"""
VoltAgent Python SDK - Comprehensive Trace and Agent Hierarchy Examples

This example demonstrates the SAME SCENARIOS as TypeScript SDK examples:
- Basic trace and agent creation (Tokyo weather)
- Multi-level agent hierarchies (Global AI research)
- Tool, memory, and retriever operations
- Error handling patterns
- Context manager usage (Python-specific)

These examples match the TypeScript SDK scenarios exactly for consistent documentation.

Run with:
    python examples/comprehensive_trace_example.py
"""

import asyncio
import os
from datetime import datetime, timezone
from typing import Any, Dict, List

# Import VoltAgent SDK
from voltagent import EventLevel, TokenUsage, VoltAgentSDK

# ===== SIMULATED EXTERNAL SERVICES =====


async def sleep(seconds: float) -> None:
    """Simulated delay for demo purposes."""
    await asyncio.sleep(seconds)


async def call_weather_api(city: str) -> Dict[str, Any]:
    """Simulated weather API call."""
    await sleep(0.5)  # API delay simulation

    # Simulated weather data - matches TypeScript SDK
    return {
        "temperature": 24,
        "condition": "rainy",
    }


async def search_web(query: str) -> List[str]:
    """Simulated web search API."""
    await sleep(0.3)
    return [
        f"Search result 1 for: {query}",
        f"Search result 2 for: {query}",
        f"Search result 3 for: {query}",
    ]


async def translate_text(text: str, target_lang: str) -> str:
    """Simulated translation service."""
    await sleep(0.4)
    return f"[{target_lang.upper()}] {text}"


# ===== EXAMPLE FUNCTIONS =====


async def basic_trace_example(sdk: VoltAgentSDK) -> None:
    """Basic Trace and Agent Example - Matches TypeScript SDK exactly."""
    print("\n🚀 Basic Trace and Agent Example Starting...")

    # Using async context manager - Python best practice!
    async with sdk.trace(
        agentId="weather-agent-v1",
        input={"query": "What's the weather in Tokyo?"},
        userId="user-123",
        conversationId="conv-456",
        tags=["weather", "basic-example"],
        metadata={
            "source": "sdk-example",
            "version": "1.0",
        },
    ) as trace:
        print(f"✅ Trace created: {trace.id}")

        # Add main agent
        agent = await trace.add_agent(
            {
                "name": "Weather Agent",
                "input": {"city": "Tokyo"},
                "instructions": "You are a weather agent. You are responsible for providing weather information to the user.",
                "metadata": {
                    "modelParameters": {
                        "model": "test-model",
                    },
                },
            }
        )
        print(f"✅ Main agent added: {agent.id}")

        # Add tool to agent
        weather_tool = await agent.add_tool(
            {
                "name": "weather-api",
                "input": {
                    "city": "Tokyo",
                    "units": "celsius",
                },
                "metadata": {
                    "apiVersion": "v2",
                    "timeout": 5000,
                },
            }
        )
        print(f"🔧 Weather tool started: {weather_tool.id}")

        # Simulate weather API call
        try:
            weather_data = await call_weather_api("Tokyo")
            await weather_tool.success(
                output={
                    "temperature": weather_data["temperature"],
                    "condition": weather_data["condition"],
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                },
                metadata={
                    "dataSource": "weather-api-v2",
                },
            )
            print(f"✅ Weather tool successful: {weather_data['temperature']}°C, {weather_data['condition']}")
        except Exception as error:
            await weather_tool.error(
                status_message=error,
                metadata={
                    "errorType": "api-failure",
                    "retryAttempted": False,
                },
            )
            print(f"❌ Weather tool error: {error}")
            return

        # Add memory operation
        memory_op = await agent.add_memory(
            {
                "name": "cache-weather-data",
                "input": {
                    "key": "weather_tokyo",
                    "value": {
                        "temp": 24,
                        "condition": "rainy",
                        "cached_at": int(datetime.now(timezone.utc).timestamp() * 1000),
                    },
                    "ttl": 3600,  # 1 hour cache
                },
                "metadata": {
                    "type": "redis",
                    "region": "ap-northeast-1",
                },
            }
        )
        print(f"💾 Memory operation started: {memory_op.id}")

        await memory_op.success(
            output={
                "cached": True,
                "key": "weather_tokyo",
                "dataSize": "124 bytes",
            },
            metadata={
                "cacheHit": False,
                "ttl": 3600,
            },
        )
        print("✅ Memory operation successful")

        # Complete agent successfully
        await agent.success(
            output={
                "response": "Weather in Tokyo is 24°C and rainy.",
                "confidence": 0.95,
                "sources": ["weather-api"],
            },
            usage=TokenUsage(prompt_tokens=45, completion_tokens=25, total_tokens=70),
        )
        print("✅ Main agent completed")

        # Trace will be automatically ended by context manager
        print(f"🎉 Trace completed: {trace.id}")


async def complex_hierarchy_example(sdk: VoltAgentSDK) -> None:
    """Complex Multi-Agent Hierarchy Example - Matches TypeScript SDK exactly."""
    print("\n🌟 Complex Multi-Agent Hierarchy Example Starting...")

    async with sdk.trace(
        agentId="research-coordinator",
        input={
            "topic": "Global AI developments and emerging trends",
            "depth": "comprehensive",
            "languages": ["en", "zh", "es"],
        },
        userId="researcher-789",
        conversationId="research-session-001",
        tags=["research", "multi-agent", "ai-trends", "global"],
        metadata={
            "priority": "high",
            "deadline": "2024-06-01",
            "requester": "research-team",
        },
    ) as trace:
        print(f"✅ Research trace created: {trace.id}")

        # Main Coordinator Agent
        coordinator = await trace.add_agent(
            {
                "name": "Research Coordinator",
                "input": {
                    "task": "Coordinate global AI research project and manage sub-agents",
                    "strategy": "divide-and-conquer",
                },
                "metadata": {
                    "role": "coordinator",
                    "experience_level": "senior",
                    "specialization": "research-management",
                    "modelParameters": {
                        "model": "gpt-4",
                    },
                },
            }
        )
        print(f"👑 Coordinator agent created: {coordinator.id}")

        # Add retriever to coordinator (for research planning)
        planning_retriever = await coordinator.add_retriever(
            {
                "name": "research-planning-retriever",
                "input": {
                    "query": "AI research methodology best practices",
                    "sources": ["academic-db", "research-guidelines"],
                    "maxResults": 10,
                },
                "metadata": {
                    "vectorStore": "pinecone",
                    "embeddingModel": "text-embedding-ada-002",
                },
            }
        )
        print(f"🔍 Planning retriever started: {planning_retriever.id}")

        await planning_retriever.success(
            output={
                "documents": [
                    "Research methodology guide for AI topics",
                    "Best practices for multi-agent coordination",
                    "Academic research standards for AI studies",
                ],
                "relevanceScores": [0.95, 0.88, 0.82],
            },
            metadata={
                "searchTime": "0.3s",
                "vectorSpace": "1536-dimensions",
            },
        )

        # SUB-AGENT 1: Data Collection Agent
        data_collector = await coordinator.add_agent(
            {
                "name": "Data Collection Agent",
                "input": {
                    "task": "Collect data about global AI developments and trends",
                    "sources": ["news", "academic-papers", "tech-reports", "industry-analysis"],
                    "timeframe": "last-2-years",
                },
                "metadata": {
                    "role": "data-collector",
                    "specialization": "global-ai-landscape",
                    "modelParameters": {
                        "model": "gpt-4",
                    },
                },
            }
        )
        print(f"📊 Data collector sub-agent created: {data_collector.id}")

        # Add web search tool to data collector
        web_search_tool = await data_collector.add_tool(
            {
                "name": "web-search-tool",
                "input": {
                    "query": "global artificial intelligence developments trends 2023 2024",
                    "searchEngine": "google",
                    "maxResults": 20,
                },
                "metadata": {
                    "searchType": "comprehensive",
                    "language": "en",
                },
            }
        )
        print(f"🔍 Web search tool started: {web_search_tool.id}")

        try:
            search_results = await search_web("global artificial intelligence developments trends")
            await web_search_tool.success(
                output={
                    "results": search_results,
                    "totalFound": len(search_results),
                    "searchTime": "0.8s",
                },
                metadata={
                    "searchEngine": "google",
                    "resultsFiltered": True,
                },
            )
            print(f"✅ Web search successful: {len(search_results)} results found")
        except Exception as error:
            await web_search_tool.error(
                status_message=error,
                metadata={
                    "searchEngine": "google",
                    "queryType": "comprehensive",
                },
            )

        # Add memory operation to data collector (store collected data)
        data_memory = await data_collector.add_memory(
            {
                "name": "collected-data-storage",
                "input": {
                    "key": "global_ai_data_2024",
                    "value": {
                        "sources": ["news-articles", "academic-papers", "tech-reports"],
                        "dataPoints": 85,
                        "lastUpdated": datetime.now(timezone.utc).isoformat(),
                    },
                    "category": "research-data",
                },
                "metadata": {
                    "storageType": "long-term",
                    "encryption": True,
                },
            }
        )
        print(f"💾 Data memory operation started: {data_memory.id}")

        await data_memory.success(
            output={
                "stored": True,
                "dataSize": "4.7MB",
                "compressionRatio": 0.65,
            },
        )

        # SUB-SUB-AGENT: Academic Paper Analyzer (under Data Collector)
        paper_analyzer = await data_collector.add_agent(
            {
                "name": "Academic Paper Analyzer",
                "input": {
                    "task": "Analyze academic papers and extract key findings from global AI research",
                    "focus": "global-ai-research-trends",
                    "analysisDepth": "detailed",
                },
                "metadata": {
                    "role": "academic-analyzer",
                    "specialization": "paper-analysis",
                    "modelParameters": {
                        "model": "gpt-4",
                    },
                },
            }
        )
        print(f"📚 Academic paper analyzer (sub-sub-agent) created: {paper_analyzer.id}")

        # Add tool to paper analyzer
        paper_analysis_tool = await paper_analyzer.add_tool(
            {
                "name": "paper-analysis-tool",
                "input": {
                    "papers": ["arxiv_paper_1.pdf", "nature_ai_2024.pdf", "ieee_ml_trends.pdf"],
                    "analysisType": "content-extraction",
                    "language": "mixed",
                },
                "metadata": {
                    "pdfParser": "advanced",
                    "nlpModel": "bert-multilingual",
                },
            }
        )
        print(f"🔬 Paper analysis tool started: {paper_analysis_tool.id}")

        await paper_analysis_tool.success(
            output={
                "analyzedPapers": 3,
                "keyFindings": [
                    "Multimodal AI systems showing 60% improvement in 2024",
                    "Enterprise AI adoption reached 70% globally",
                    "Significant breakthroughs in AI safety and alignment",
                ],
                "confidence": 0.89,
            },
            metadata={
                "processingTime": "12.3s",
                "nlpModel": "bert-multilingual-v2",
            },
        )

        # Complete paper analyzer
        await paper_analyzer.success(
            output={
                "summary": "3 academic papers analyzed successfully",
                "keyInsights": ["Multimodal AI advances", "Enterprise adoption growth", "AI safety progress"],
                "nextSteps": ["Deep dive into multimodal research", "Enterprise case studies analysis"],
            },
            metadata={
                "totalPapersProcessed": 3,
                "analysisAccuracy": 0.94,
            },
        )

        # SUB-AGENT 2: Translation Agent
        translator = await coordinator.add_agent(
            {
                "name": "Translation Agent",
                "input": {
                    "task": "Translate collected data to multiple languages",
                    "sourceLanguage": "english",
                    "targetLanguages": ["spanish", "chinese", "french"],
                    "preserveTerminology": True,
                },
                "metadata": {
                    "role": "translator",
                    "specialization": "technical-translation",
                    "languages": ["en", "es", "zh", "fr"],
                    "modelParameters": {
                        "model": "gpt-4",
                    },
                },
            }
        )
        print(f"🌍 Translation sub-agent created: {translator.id}")

        # Add translation tool
        translation_tool = await translator.add_tool(
            {
                "name": "ai-translation-tool",
                "input": {
                    "text": "Multimodal AI systems are showing significant improvements in 2024",
                    "fromLang": "en",
                    "toLang": "es",
                    "domain": "technology",
                },
                "metadata": {
                    "model": "neural-translation-v3",
                    "qualityCheck": True,
                },
            }
        )
        print(f"🔤 Translation tool started: {translation_tool.id}")

        try:
            translated_text = await translate_text(
                "Multimodal AI systems are showing significant improvements in 2024", "es"
            )
            await translation_tool.success(
                output={
                    "translatedText": translated_text,
                    "confidence": 0.96,
                    "wordCount": 10,
                },
                metadata={
                    "model": "neural-translation-v3",
                },
            )
            print(f"✅ Translation successful: {translated_text}")
        except Exception as error:
            await translation_tool.error(
                status_message=error,
                metadata={
                    "translationPair": "en-es",
                    "model": "neural-translation-v3",
                },
            )

        # SUB-SUB-AGENT: Quality Checker (under Translator)
        quality_checker = await translator.add_agent(
            {
                "name": "Translation Quality Control Agent",
                "input": {
                    "task": "Check translation quality and suggest improvements",
                    "criteria": ["accuracy", "fluency", "terminology"],
                    "threshold": 0.9,
                },
                "metadata": {
                    "role": "quality-checker",
                    "specialization": "translation-qa",
                    "modelParameters": {
                        "model": "gpt-4",
                    },
                },
            }
        )
        print(f"✅ Quality checker (sub-sub-agent) created: {quality_checker.id}")

        # Add retriever to quality checker (for terminology verification)
        terminology_retriever = await quality_checker.add_retriever(
            {
                "name": "ai-terminology-retriever",
                "input": {
                    "query": "AI technical terms multilingual translation verification",
                    "domain": "artificial-intelligence",
                    "verificationMode": True,
                },
                "metadata": {
                    "terminologyDB": "global-tech-terms-v3",
                    "languages": ["en", "es", "zh", "fr"],
                },
            }
        )
        print(f"📖 Terminology retriever started: {terminology_retriever.id}")

        await terminology_retriever.success(
            output={
                "verifiedTerms": [
                    "multimodal AI -> IA multimodal (es)",
                    "artificial intelligence -> inteligencia artificial (es)",
                    "machine learning -> aprendizaje automático (es)",
                ],
                "accuracy": 0.98,
            },
            metadata={
                "databaseVersion": "global-tech-terms-v3",
            },
        )

        # Complete quality checker
        await quality_checker.success(
            output={
                "qualityScore": 0.94,
                "issues": [],
                "recommendations": ["Excellent translation quality", "Terminology consistency maintained"],
            },
            usage=TokenUsage(prompt_tokens=120, completion_tokens=80, total_tokens=200),
            metadata={
                "criteriaChecked": 3,
            },
        )

        # Complete translator
        await translator.success(
            output={
                "translationCompleted": True,
                "totalWords": 250,
                "averageQuality": 0.94,
            },
            usage=TokenUsage(prompt_tokens=350, completion_tokens=180, total_tokens=530),
            metadata={
                "languagePairs": ["en-es", "en-zh", "en-fr"],
                "qualityThreshold": 0.9,
            },
        )

        # Complete data collector
        await data_collector.success(
            output={
                "dataCollected": True,
                "totalSources": 25,
                "keyDataPoints": 45,
            },
            usage=TokenUsage(prompt_tokens=450, completion_tokens=280, total_tokens=730),
            metadata={
                "subAgentsUsed": 1,
                "analysisAccuracy": 0.91,
            },
        )

        # Add final memory operation to coordinator
        final_results = await coordinator.add_memory(
            {
                "name": "final-research-results",
                "input": {
                    "key": "global_ai_research_final",
                    "value": {
                        "dataPoints": 85,
                        "translations": 250,
                        "qualityScore": 0.94,
                        "completedAt": datetime.now(timezone.utc).isoformat(),
                    },
                    "category": "final-results",
                },
                "metadata": {
                    "storageType": "permanent",
                    "backup": True,
                },
            }
        )
        print(f"💾 Final results memory started: {final_results.id}")

        await final_results.success(
            output={
                "stored": True,
                "archived": True,
                "backupLocation": "s3://research-backups/",
            },
            metadata={
                "storageProvider": "aws-s3",
            },
        )

        # Complete coordinator
        await coordinator.success(
            output={
                "projectCompleted": True,
                "subAgentsManaged": 2,
                "totalOperations": 8,
                "overallSuccess": True,
                "summary": "Global AI research completed successfully",
                "recommendations": [
                    "Continue monitoring global AI development trends",
                    "Schedule follow-up research in 6 months",
                    "Share findings with international research community",
                ],
            },
            usage=TokenUsage(prompt_tokens=1200, completion_tokens=850, total_tokens=2050),
            metadata={
                "successRate": 1.0,
            },
        )
        print("👑 Coordinator agent completed")

        # Trace will be automatically ended with success by context manager
        print(f"🎉 Complex hierarchy trace completed: {trace.id}")


async def error_handling_example(sdk: VoltAgentSDK) -> None:
    """Error Handling Example - Matches TypeScript SDK exactly."""
    print("\n⚠️ Error Handling Example Starting...")

    try:
        async with sdk.trace(agentId="error-test-agent", input={"testType": "error-scenarios"}) as trace:
            agent = await trace.add_agent({"name": "Error Test Agent", "input": {"scenario": "api-failure"}})

            # Failed tool example
            failing_tool = await agent.add_tool(
                {"name": "failing-api-tool", "input": {"endpoint": "https://nonexistent-api.com/data"}}
            )

            # Simulated API failure
            await failing_tool.error(
                status_message=Exception("API endpoint not reachable"),
                metadata={
                    "endpoint": "https://nonexistent-api.com/data",
                    "httpStatus": 404,
                },
            )
            print("❌ Tool error recorded")

            # Mark agent as failed as well
            await agent.error(
                status_message=Exception("Agent failed due to tool failure"),
                metadata={
                    "failedTool": failing_tool.id,
                    "errorCategory": "api_failure",
                },
            )
            print("❌ Agent error recorded")

            # Note: Trace will be automatically ended with error by context manager
            print("❌ Trace terminated with error")

    except Exception as e:
        print(f"❌ Error handling example error: {e}")


# ===== MAIN FUNCTION =====


async def main() -> None:
    """Main function demonstrating all SDK features - matches TypeScript examples."""
    print("🌟 VoltAgent SDK - Comprehensive Trace and Agent Hierarchy Examples")
    print("=" * 70)

    # Initialize SDK
    sdk = VoltAgentSDK(
        base_url=os.getenv("VOLTAGENT_BASE_URL", "https://api.voltagent.dev"),
        public_key=os.getenv("VOLTAGENT_PUBLIC_KEY", "demo-public-key"),
        secret_key=os.getenv("VOLTAGENT_SECRET_KEY", "demo-secret-key"),
        auto_flush=True,
        flush_interval=3,  # Send every 3 seconds
        timeout=30,
    )

    try:
        # Run examples - matches TypeScript SDK order
        await basic_trace_example(sdk)
        await complex_hierarchy_example(sdk)
        await error_handling_example(sdk)

        print("\n✅ All examples completed!")

        # Final flush operation
        await sdk.flush()
        print("📤 All events sent")

    except Exception as e:
        print(f"❌ Main function error: {e}")
    finally:
        # Cleanup SDK resources
        await sdk.shutdown()
        print("🔒 SDK shutdown")


# ===== ENTRY POINT =====

if __name__ == "__main__":
    """
    Run the examples - matches TypeScript SDK scenarios exactly.

    Set environment variables:
    export VOLTAGENT_BASE_URL="https://api.voltagent.dev"
    export VOLTAGENT_PUBLIC_KEY="your-public-key"
    export VOLTAGENT_SECRET_KEY="your-secret-key"

    Then run:
    python examples/comprehensive_trace_example.py
    """
    asyncio.run(main())
