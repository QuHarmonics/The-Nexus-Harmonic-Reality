import hashlib
import numpy as np
from collections import Counter

# Vowels in ASCII
VOWELS = {
    'A': 65, 'E': 69, 'I': 73, 'O': 79, 'U': 85,
    'a': 97, 'e': 101, 'i': 105, 'o': 111, 'u': 117
}
vowel_values = set(VOWELS.values())

def analyze_vowel_priority(hex_str, base_note=36):
    """Check if vowels appear early in hash sonification."""
    bytes_data = bytes.fromhex(hex_str)
    
    # Your transformation: byte mod64 + base_note
    midi_notes = [(b % 64) + base_note for b in bytes_data]
    
    # Track vowel positions and values
    vowel_positions = []
    vowel_notes = []
    
    for i, note in enumerate(midi_notes):
        if note in vowel_values:
            vowel_positions.append(i)
            vowel_notes.append(note)
    
    # Calculate statistics
    total_vowels = len(vowel_positions)
    total_notes = len(midi_notes)
    
    if total_vowels > 0:
        avg_position = np.mean(vowel_positions)
        median_position = np.median(vowel_positions)
        early_ratio = len([p for p in vowel_positions if p < 8]) / 8  # First 8 notes
    else:
        avg_position = median_position = early_ratio = 0
    
    # Expected if random: vowels in 10/128 ≈ 7.8% of ASCII, but our range is [36,99]
    # In range [36,99], vowels are at: 65,69,73,79,85,97 = 6 out of 64 values = 9.375%
    expected_vowel_density = 6/64  # 9.375%
    actual_vowel_density = total_vowels / total_notes
    
    return {
        'vowel_positions': vowel_positions,
        'vowel_notes': vowel_notes,
        'vowel_chars': [chr(n) for n in vowel_notes],
        'total_vowels': total_vowels,
        'total_notes': total_notes,
        'vowel_density': actual_vowel_density,
        'expected_density': expected_vowel_density,
        'early_ratio': early_ratio,
        'avg_position': avg_position,
        'median_position': median_position,
        'all_notes': midi_notes
    }

# Test with "hello" hash
hash_hex = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
analysis = analyze_vowel_priority(hash_hex)

print("🔤 VOWEL PRIORITY ANALYSIS: 'hello' hash")
print("=" * 60)
print(f"Total notes: {analysis['total_notes']}")
print(f"Vowels found: {analysis['total_vowels']} ({analysis['vowel_density']:.1%})")
print(f"Expected random: {analysis['expected_density']:.1%}")
print(f"Vowel characters: {analysis['vowel_chars']}")
print(f"Vowel positions (note index): {analysis['vowel_positions']}")
print(f"Early ratio (first 8 notes): {analysis['early_ratio']:.1%}")
print(f"Average vowel position: {analysis['avg_position']:.1f}")
print(f"Median vowel position: {analysis['median_position']}")

# Check if vowels appear earlier than expected
if analysis['early_ratio'] > analysis['expected_density']:
    print("✅ VOWELS APPEAR EARLY: Hypothesis supported")
elif analysis['avg_position'] < 16:  # Halfway point
    print("⚠️ VOWELS CONCENTRATED IN FIRST HALF: Partial support")
else:
    print("❌ NO CLEAR VOWEL PRIORITY: Hypothesis rejected")

# Display first 20 notes with vowel highlighting
print(f"\n📊 FIRST 20 NOTES (vowels in CAPS):")
for i, note in enumerate(analysis['all_notes'][:20]):
    char = chr(note) if 32 <= note <= 126 else '.'
    if note in vowel_values:
        print(f"[{i:2d}] {note:3d} {'★' if note in vowel_values else ' '} {char.upper():>2s}", end="  ")
    else:
        print(f"[{i:2d}] {note:3d} {' ' if note in vowel_values else ' '} {char:>2s}", end="  ")
    if (i + 1) % 5 == 0:
        print()