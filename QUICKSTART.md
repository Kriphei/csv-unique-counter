# Quick Start Guide - Get Mac & Windows Executables

## 🎯 Goal
Create executables for **both Windows and Mac** without needing a Mac computer.

## ✅ What's Been Set Up

1. ✅ Python script (`csv_unique_counter.py`) - works cross-platform
2. ✅ Windows executable (`dist/CSV_Unique_Counter.exe`) - ready to use
3. ✅ GitHub Actions workflow - builds both platforms automatically
4. ✅ All necessary configuration files

## 🚀 Next Steps (5 Minutes)

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Name: `csv-unique-counter`
3. Click "Create repository"

### Step 2: Upload Files to GitHub

**Easy Way (Web Interface):**
1. Click "uploading an existing file" on GitHub
2. Drag and drop these files/folders:
   - `csv_unique_counter.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
   - `.github` folder (entire folder)
3. Click "Commit changes"

**Command Line Way:**
```bash
cd "G:\Shared drives\Finance - Sales (Internal)"
git init
git add csv_unique_counter.py requirements.txt README.md .gitignore .github/
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/csv-unique-counter.git
git branch -M main
git push -u origin main
```

### Step 3: Wait for Build (5-10 minutes)
GitHub Actions will automatically:
- Build Windows executable
- Build Mac executable
- Create a release with both files

### Step 4: Download Your Executables

Go to your repository → **Releases** section → Download:
- `CSV_Unique_Counter_Windows.exe` (Windows)
- `CSV_Unique_Counter_Mac` (Mac)

## 📦 Distribute to Your Team

### Windows Users:
"Download CSV_Unique_Counter_Windows.exe and double-click to run!"

### Mac Users:
"Download CSV_Unique_Counter_Mac, right-click → Open to run!"

## 🔄 Making Updates

Whenever you update the code:
```bash
git add csv_unique_counter.py
git commit -m "Updated feature"
git push
```

GitHub Actions will automatically rebuild both executables!

## 📚 More Information

- Full setup guide: [GITHUB_SETUP.md](GITHUB_SETUP.md)
- Usage instructions: [README.md](README.md)

## ⚡ Benefits

✅ No Mac needed to build Mac executables  
✅ Completely free (GitHub Actions)  
✅ Automatic builds on every update  
✅ Version control included  
✅ Team can use without Python installed  

---

**That's it!** Once set up, you'll have executables for both platforms, updated automatically with every code change.

