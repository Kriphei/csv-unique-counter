# GitHub Actions Setup Guide

This guide will help you set up automated building of Windows and Mac executables using GitHub Actions (completely free!).

## 🚀 Quick Setup (5 Minutes)

### Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in (or create a free account)
2. Click the **"+"** icon in the top right → **"New repository"**
3. Name it: `csv-unique-counter` (or any name you prefer)
4. Choose **Public** or **Private** (both work with Actions)
5. Click **"Create repository"**

### Step 2: Upload Your Code

You have two options:

#### Option A: Using Git (Command Line)

```bash
# Navigate to your project folder
cd "G:\Shared drives\Finance - Sales (Internal)"

# Initialize git repository
git init

# Add all files
git add csv_unique_counter.py requirements.txt .github/ .gitignore README.md

# Commit files
git commit -m "Initial commit - CSV Unique Counter"

# Connect to GitHub (replace YOUR_USERNAME and YOUR_REPO)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to GitHub
git branch -M main
git push -u origin main
```

#### Option B: Using GitHub Web Interface (Easier)

1. On your new GitHub repository page, click **"uploading an existing file"**
2. Drag and drop these files:
   - `csv_unique_counter.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
   - The entire `.github` folder
3. Click **"Commit changes"**

### Step 3: Run the Build

Once uploaded, GitHub Actions will automatically:
1. Detect the workflow file
2. Start building executables for Windows and Mac
3. This takes about 5-10 minutes

To check progress:
1. Go to your repository on GitHub
2. Click the **"Actions"** tab
3. Watch the build process

### Step 4: Download Your Executables

#### Option A: From Artifacts (Available Immediately)

1. Go to **Actions** tab
2. Click on the latest successful workflow run
3. Scroll down to **"Artifacts"** section
4. Download:
   - `CSV_Unique_Counter_Windows` (for Windows users)
   - `CSV_Unique_Counter_Mac` (for Mac users)

#### Option B: From Releases (Automatic)

If you pushed to the main/master branch:
1. Go to your repository main page
2. Click **"Releases"** on the right sidebar
3. The latest release will have both executables attached
4. Download and distribute to your team!

## 🔄 Updating the Program

Whenever you make changes:

```bash
# Make your code changes to csv_unique_counter.py

# Commit and push
git add csv_unique_counter.py
git commit -m "Updated feature X"
git push

# GitHub Actions will automatically build new executables!
```

## 🎯 Manual Trigger

You can also manually trigger a build:
1. Go to **Actions** tab
2. Click **"Build Executables"** workflow
3. Click **"Run workflow"** button
4. Select branch and click **"Run workflow"**

## 📦 Distributing to Your Team

### For Windows Users:
1. Download `CSV_Unique_Counter_Windows.exe`
2. Double-click to run
3. No installation needed!

### For Mac Users:
1. Download `CSV_Unique_Counter_Mac`
2. Right-click → Open (first time only, to bypass Gatekeeper)
3. Or run from terminal: `chmod +x CSV_Unique_Counter_Mac && ./CSV_Unique_Counter_Mac`

## ⚡ Benefits

- ✅ **Free**: GitHub Actions is free for public repos (2,000 minutes/month for private repos)
- ✅ **Automated**: Build both platforms with one push
- ✅ **No Mac needed**: Builds Mac executables in the cloud
- ✅ **Version control**: Track all changes
- ✅ **Easy updates**: Push code → Get new executables

## 🔧 Troubleshooting

**Build fails?**
- Check the Actions tab for error messages
- Make sure `csv_unique_counter.py` is in the repository root
- Verify Python syntax is correct

**Mac executable won't open?**
- Mac users need to right-click → Open (security feature)
- Or enable in System Preferences → Security & Privacy

**Need help?**
- Check the Actions logs for detailed error messages
- GitHub Actions documentation: https://docs.github.com/en/actions

## 📝 Notes

- Executables are kept for 90 days in Artifacts
- Releases are permanent
- Each push to main/master creates a new release automatically
- You can customize the workflow in `.github/workflows/build-executables.yml`

