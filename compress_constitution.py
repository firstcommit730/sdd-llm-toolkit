#!/usr/bin/env python3
"""
Compress constitution.md by converting verbose multi-line structures to inline pipe-separated format.
"""

import re
import sys

def compress_list_to_inline(lines):
    """Convert bulleted lists to inline pipe-separated format."""
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a list item with sub-bullets
        if line.strip().startswith('- **') and ':' in line:
            # Collect all related list items
            items = []
            while i < len(lines) and lines[i].strip().startswith('- **'):
                items.append(lines[i].strip()[2:])  # Remove '- '
                i += 1
            
            # Join with pipe separator
            result.append(' | '.join(items))
            continue
        
        result.append(line)
        i += 1
    
    return result

def compress_numbered_list(lines):
    """Convert numbered lists with sub-bullets to inline format."""
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for numbered list pattern like "1. **Name**"
        if re.match(r'^\d+\.\s+\*\*', line.strip()):
            # Extract the number and content
            match = re.match(r'^(\d+)\.\s+(.+)$', line.strip())
            if match:
                num, content = match.groups()
                
                # Check if next lines are sub-bullets
                sub_items = [content]
                i += 1
                while i < len(lines) and lines[i].strip().startswith('- **'):
                    sub_items.append(lines[i].strip()[2:])  # Remove '- '
                    i += 1
                
                # Create compressed format
                result.append(f"**{num}. {' | '.join(sub_items)}**")
                continue
        
        result.append(line)
        i += 1
    
    return result

def compress_section_headers(lines):
    """Compress section headers with sub-items."""
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for header followed by description list
        if line.strip().startswith('####') and i + 1 < len(lines):
            header = line.strip()
            i += 1
            
            # Collect following list items
            items = []
            while i < len(lines) and lines[i].strip().startswith('- **'):
                items.append(lines[i].strip()[2:])  # Remove '- '
                i += 1
            
            if items:
                # Create inline format
                header_text = header.replace('####', '').strip()
                result.append(f"**{header_text}**: {' | '.join(items)}")
            else:
                result.append(header)
            continue
        
        result.append(line)
        i += 1
    
    return result

def main():
    input_file = '.specify/memory/constitution.md'
    output_file = '.specify/memory/constitution.md.compressed'
    
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Apply compression transformations
    lines = [line.rstrip() for line in lines]  # Remove trailing whitespace
    lines = compress_list_to_inline(lines)
    lines = compress_numbered_list(lines)
    lines = compress_section_headers(lines)
    
    # Remove excessive blank lines (more than 2 consecutive)
    result = []
    blank_count = 0
    for line in lines:
        if not line.strip():
            blank_count += 1
            if blank_count <= 2:
                result.append(line)
        else:
            blank_count = 0
            result.append(line)
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(result))
    
    print(f"Compressed {len(lines)} lines to {len(result)} lines")
    print(f"Output written to: {output_file}")

if __name__ == '__main__':
    main()
