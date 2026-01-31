#!/usr/bin/env python3
"""
Digital Garden Front Matter Updater

This script helps you add or update front matter in your markdown files
for the new garden-themed layout.

Usage:
    python3 update_frontmatter.py [--dry-run] [--category CATEGORY] [--icon ICON]

Options:
    --dry-run          Show what would be changed without making changes
    --category CAT     Set default category (default: learning)
    --icon ICON        Set default growth icon (default: 🌱)
    --content-dir DIR  Path to content directory (default: content)
"""

import os
import re
import argparse
from pathlib import Path
from datetime import datetime
import yaml

# Category detection keywords
CATEGORY_KEYWORDS = {
    'books': ['book', 'reading', 'read', 'author', 'novel', 'literature'],
    'philosophy': ['philosophy', 'stoicism', 'ethics', 'philosopher', 'socrates', 'plato', 'aristotle'],
    'science': ['science', 'biology', 'physics', 'chemistry', 'research', 'study'],
    'technology': ['code', 'programming', 'software', 'tech', 'aws', 'python', 'javascript', 'data'],
    'learning': ['learn', 'study', 'education', 'course', 'tutorial'],
    'finance': ['finance', 'investment', 'stock', 'trading', 'money', 'economics']
}

# Growth stage heuristics (based on word count)
def determine_growth_stage(content):
    """Determine growth stage based on content length and structure"""
    word_count = len(content.split())
    
    if word_count < 100:
        return '🌱'  # Seed
    elif word_count < 500:
        return '🌿'  # Sapling
    elif word_count < 1500:
        return '🪴'  # Plant
    else:
        return '🌳'  # Tree

def detect_category(title, content, tags):
    """Detect category based on title, content, and tags"""
    text = (title + ' ' + content + ' ' + ' '.join(tags)).lower()
    
    scores = {}
    for category, keywords in CATEGORY_KEYWORDS.items():
        score = sum(1 for keyword in keywords if keyword in text)
        scores[category] = score
    
    # Return category with highest score, or 'learning' as default
    best_category = max(scores, key=scores.get)
    return best_category if scores[best_category] > 0 else 'learning'

def extract_front_matter(content):
    """Extract front matter from markdown content"""
    if not content.startswith('---'):
        return {}, content
    
    try:
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = yaml.safe_load(parts[1])
            remaining_content = parts[2].strip()
            return front_matter or {}, remaining_content
    except:
        pass
    
    return {}, content

def process_file(file_path, args):
    """Process a single markdown file"""
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract existing front matter
    front_matter, body = extract_front_matter(content)
    
    # Determine title
    if 'title' not in front_matter:
        # Try to extract from first heading
        heading_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
        if heading_match:
            front_matter['title'] = heading_match.group(1)
        else:
            # Use filename
            front_matter['title'] = file_path.stem.replace('-', ' ').replace('_', ' ').title()
    
    # Set date if not present
    if 'date' not in front_matter:
        # Use file modification time
        mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
        front_matter['date'] = mtime.strftime('%Y-%m-%d')
    
    # Get tags
    tags = front_matter.get('tags', [])
    if isinstance(tags, str):
        tags = [tags]
    
    # Detect or set category
    if 'category' not in front_matter:
        detected_category = detect_category(
            front_matter.get('title', ''),
            body,
            tags
        )
        front_matter['category'] = args.category or detected_category
    
    # Determine growth icon
    if 'growthIcon' not in front_matter:
        if args.icon:
            front_matter['growthIcon'] = args.icon
        else:
            front_matter['growthIcon'] = determine_growth_stage(body)
    
    # Ensure tags is a list
    if tags and 'tags' not in front_matter:
        front_matter['tags'] = tags
    elif not tags:
        front_matter['tags'] = []
    
    # Build new content
    new_content = '---\n'
    new_content += yaml.dump(front_matter, default_flow_style=False, allow_unicode=True)
    new_content += '---\n\n'
    new_content += body
    
    if args.dry_run:
        print(f"  Would update with:")
        print(f"    - Title: {front_matter.get('title')}")
        print(f"    - Category: {front_matter.get('category')}")
        print(f"    - Growth Icon: {front_matter.get('growthIcon')}")
        print(f"    - Tags: {', '.join(front_matter.get('tags', []))}")
    else:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✓ Updated")
    
    return front_matter

def main():
    parser = argparse.ArgumentParser(
        description='Add or update front matter in markdown files for Digital Garden'
    )
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be changed without making changes')
    parser.add_argument('--category', type=str,
                        help='Default category for notes without category')
    parser.add_argument('--icon', type=str,
                        help='Default growth icon (🌱, 🌿, 🪴, 🌳)')
    parser.add_argument('--content-dir', type=str, default='content',
                        help='Path to content directory')
    
    args = parser.parse_args()
    
    content_dir = Path(args.content_dir)
    
    if not content_dir.exists():
        print(f"Error: Content directory '{content_dir}' not found!")
        print("Make sure you're running this from your Hugo site root directory.")
        return
    
    print(f"\n{'DRY RUN - ' if args.dry_run else ''}Processing markdown files in {content_dir}\n")
    
    # Find all markdown files
    md_files = list(content_dir.rglob('*.md'))
    
    if not md_files:
        print(f"No markdown files found in {content_dir}")
        return
    
    print(f"Found {len(md_files)} markdown files\n")
    
    # Statistics
    categories = {}
    growth_stages = {}
    
    # Process each file
    for md_file in md_files:
        try:
            front_matter = process_file(md_file, args)
            
            # Collect stats
            cat = front_matter.get('category', 'unknown')
            categories[cat] = categories.get(cat, 0) + 1
            
            icon = front_matter.get('growthIcon', '🌱')
            growth_stages[icon] = growth_stages.get(icon, 0) + 1
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    # Print summary
    print(f"\n{'=' * 50}")
    print("Summary")
    print(f"{'=' * 50}\n")
    
    print("Categories:")
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {count}")
    
    print("\nGrowth Stages:")
    stage_names = {
        '🌱': 'Seeds',
        '🌿': 'Saplings',
        '🪴': 'Plants',
        '🌳': 'Trees'
    }
    for icon, count in sorted(growth_stages.items()):
        name = stage_names.get(icon, 'Unknown')
        print(f"  {icon} {name}: {count}")
    
    if args.dry_run:
        print("\n⚠️  This was a dry run. No files were modified.")
        print("Run without --dry-run to apply changes.")
    else:
        print("\n✓ All files processed successfully!")

if __name__ == '__main__':
    main()
