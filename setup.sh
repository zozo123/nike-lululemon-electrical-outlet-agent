#!/bin/bash
# Smart Shopping Assistant Setup Script
# This script uses uv for Python dependency management

echo "🛒 Setting up Smart Shopping Assistant..."

# Initialize Git submodules (Steel Browser)
echo "📥 Initializing Steel Browser submodule..."
if [ -d "steel-browser" ] && [ ! "$(ls -A steel-browser)" ]; then
    echo "  Steel Browser directory exists but is empty, initializing..."
    git submodule update --init --recursive steel-browser
elif [ ! -d "steel-browser" ]; then
    echo "  Steel Browser not found, initializing submodule..."
    git submodule update --init --recursive steel-browser
else
    echo "  ✅ Steel Browser already initialized"
fi

# Update submodule to latest
echo "🔄 Updating Steel Browser to latest version..."
git submodule update --remote steel-browser
echo "  ✅ Steel Browser updated to latest"

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "✅ .env file created. Please edit it with your API keys."
    echo ""
    echo "Required API keys:"
    echo "  - GEMINI_API_KEY: Get from https://aistudio.google.com/"
    echo "  - STEEL_API_KEY: Get from your Steel Browser dashboard"
    echo ""
else
    echo "✅ .env file already exists"
fi

# Install Python dependencies using uv
echo "📦 Installing Python dependencies with uv..."
if command -v uv &> /dev/null; then
    uv sync
    echo "  ✅ Python dependencies installed successfully"
else
    echo "  ❌ uv not found! Please install uv first:"
    echo "     curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "     Then run this setup script again."
    exit 1
fi

# Setup Steel Browser with Docker (no npm needed!)
echo "� Setting up Steel Browser with Docker..."
cd steel-browser
if [ -f "docker-compose.yml" ]; then
    echo "  Building and starting Steel Browser with Docker..."
    docker compose up -d --build
    echo "  ✅ Steel Browser is running at http://localhost:3000"
else
    echo "  ⚠️ docker-compose.yml not found in steel-browser directory"
    echo "  Please ensure the steel-browser submodule is properly initialized"
fi
cd ..

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📋 Steel Browser is now running in the background!"
echo "💡 This project uses uv for Python dependency management - no npm needed!"
echo ""
echo "🚀 Quick Start:"
echo "   uv run smart_shop.py"
echo ""
echo "🔧 Manage Steel Browser:"
echo "   Stop:    cd steel-browser && docker compose down"
echo "   Restart: cd steel-browser && docker compose restart"
echo "   Logs:    cd steel-browser && docker compose logs -f"
echo ""
echo "🐳 Steel Browser API: http://localhost:3000"
echo "🛒 The shopping assistant finds the best deals across Nike, Lululemon & PaynGo!"
