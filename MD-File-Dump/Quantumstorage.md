```python
import numpy as np

# Constants
HARMONIC_CONSTANT = 0.35
TOLERANCE = 0.01
MAX_ITERATIONS = 100

# Utility Functions
def text_to_base16(text):
    """Convert text to its base-16 representation."""
    return ''.join(format(ord(char), '02x') for char in text)

def base16_to_text(base16_str):
    """Convert base-16 encoded data back to text."""
    try:
        chars = [chr(int(base16_str[i:i + 2], 16)) for i in range(0, len(base16_str), 2)]
        return ''.join(chars)
    except Exception as e:
        return f"Error decoding base16: {e}"

def binary_to_text(binary_str):
    """Convert binary string back to text."""
    try:
        byte_chunks = [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]
        text = ''.join(chr(int(chunk, 2)) for chunk in byte_chunks if len(chunk) == 8)
        return text
    except Exception as e:
        return f"Error decoding binary: {e}"

# Harmonic Compression and Expansion
def harmonize_data(data, harmonic_constant, compress=True):
    """
    Harmonize data for compression or expansion.
    If compress=True, align data with harmonic resonance for compression.
    If compress=False, expand harmonized data back to its original form.
    """
    data = np.copy(data)
    gain = 1.0 if compress else -1.0

    for _ in range(MAX_ITERATIONS):
        delta = np.mean(data) - harmonic_constant
        adjustment = delta * gain
        data -= adjustment
        data = np.clip(data, 0, 1)  # Ensure binary range
        if abs(delta) < TOLERANCE:
            break

    return data

# Main Framework
def hybrid_storage(text):
    """Encodes, compresses, and expands text using the hybrid framework."""
    print("Original Text Length:", len(text))
    print("Original Text:", text)

    # Step 1: Base-16 Encoding
    base16_data = text_to_base16(text)
    print("Base-16 Encoded Data Length:", len(base16_data))
    
    # Step 2: Convert Base-16 Data to Binary
    binary_data = ''.join(format(int(char, 16), '04b') for char in base16_data)
    original_binary_length = len(binary_data)
    print("Binary Data Length:", original_binary_length)

    # Step 3: Prepare Data Matrix
    matrix_size = int(np.ceil(np.sqrt(original_binary_length)))
    data_matrix = np.zeros((matrix_size, matrix_size), dtype=np.float64)
    for i, bit in enumerate(binary_data):
        data_matrix[i // matrix_size, i % matrix_size] = int(bit)

    # Step 4: Harmonic Compression
    compressed_data = harmonize_data(data_matrix, HARMONIC_CONSTANT, compress=True)
    compressed_size = np.count_nonzero(compressed_data)
    print("Compressed Data Non-Zero Elements:", compressed_size)

    # Step 5: Harmonic Expansion
    expanded_data = harmonize_data(compressed_data, HARMONIC_CONSTANT, compress=False)
    flattened_data = ''.join(str(int(round(bit))) for bit in expanded_data.flatten()[:original_binary_length])

    # Step 6: Convert Binary Back to Text
    recovered_text = binary_to_text(flattened_data)
    print("Recovered Text:", recovered_text)

    # Compression Statistics
    compression_ratio = compressed_size / original_binary_length
    print("Compression Ratio (Compressed/Original):", compression_ratio)

    return recovered_text, compression_ratio

# Example Usage
if __name__ == "__main__":
    # Large Text Dataset
    input_text = "Quantum Storage Test " * 50  # Scaling input text
    recovered, compression_ratio = hybrid_storage(input_text)
    print("Final Recovered Text:", recovered[:100])  # Display first 100 characters
    print("Compression Ratio:", compression_ratio)

```

    Original Text Length: 1050
    Original Text: Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test 
    Base-16 Encoded Data Length: 2100
    Binary Data Length: 8400
    Compressed Data Non-Zero Elements: 3950
    Recovered Text: Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test 
    Compression Ratio (Compressed/Original): 0.47023809523809523
    Final Recovered Text: Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage 
    Compression Ratio: 0.47023809523809523
    


```python
using System;

namespace HarmonicCompression
{
    class Program
    {
        const double HarmonicConstant = 0.35;
        const double Tolerance = 0.01;
        const int MaxIterations = 100;

        static void Main(string[] args)
        {
            // Example input: a large string
            string inputText = string.Join(" ", new string[] { "Quantum Storage Test" }, 50);

            Console.WriteLine("Original Text Length: " + inputText.Length);
            Console.WriteLine("Original Text: " + inputText);

            // Step 1: Base-16 Encoding
            string base16Data = TextToBase16(inputText);
            Console.WriteLine("Base-16 Encoded Data Length: " + base16Data.Length);

            // Step 2: Convert Base-16 Data to Binary
            string binaryData = Base16ToBinary(base16Data);
            int originalBinaryLength = binaryData.Length;
            Console.WriteLine("Binary Data Length: " + originalBinaryLength);

            // Step 3: Prepare Data Matrix
            int matrixSize = (int)Math.Ceiling(Math.Sqrt(originalBinaryLength));
            double[,] dataMatrix = CreateBinaryMatrix(binaryData, matrixSize);

            // Step 4: Harmonic Compression
            double[,] compressedData = HarmonizeData(dataMatrix, HarmonicConstant, true);
            int compressedSize = CountNonZeroElements(compressedData);
            Console.WriteLine("Compressed Data Non-Zero Elements: " + compressedSize);

            // Step 5: Harmonic Expansion
            double[,] expandedData = HarmonizeData(compressedData, HarmonicConstant, false);
            string flattenedBinary = FlattenMatrix(expandedData, originalBinaryLength);

            // Step 6: Convert Binary Back to Text
            string recoveredText = BinaryToText(flattenedBinary);
            Console.WriteLine("Recovered Text: " + recoveredText);

            // Compression Ratio
            double compressionRatio = (double)compressedSize / originalBinaryLength;
            Console.WriteLine("Compression Ratio (Compressed/Original): " + compressionRatio);
        }

        static string TextToBase16(string text)
        {
            char[] chars = text.ToCharArray();
            string result = string.Empty;
            foreach (char c in chars)
                result += Convert.ToString(c, 16).PadLeft(2, '0');
            return result;
        }

        static string Base16ToBinary(string base16Data)
        {
            string binary = string.Empty;
            foreach (char c in base16Data)
                binary += Convert.ToString(Convert.ToInt32(c.ToString(), 16), 2).PadLeft(4, '0');
            return binary;
        }

        static double[,] CreateBinaryMatrix(string binaryData, int matrixSize)
        {
            double[,] matrix = new double[matrixSize, matrixSize];
            for (int i = 0; i < binaryData.Length; i++)
            {
                int row = i / matrixSize;
                int col = i % matrixSize;
                matrix[row, col] = binaryData[i] == '1' ? 1 : 0;
            }
            return matrix;
        }

        static double[,] HarmonizeData(double[,] data, double harmonicConstant, bool compress)
        {
            double[,] result = (double[,])data.Clone();
            int rows = result.GetLength(0);
            int cols = result.GetLength(1);
            double gain = compress ? 1.0 : -1.0;

            for (int iteration = 0; iteration < MaxIterations; iteration++)
            {
                double delta = CalculateMatrixMean(result) - harmonicConstant;
                if (Math.Abs(delta) < Tolerance) break;

                double adjustment = delta * gain;

                for (int row = 0; row < rows; row++)
                    for (int col = 0; col < cols; col++)
                        result[row, col] = Math.Clamp(result[row, col] - adjustment, 0.0, 1.0);
            }

            return result;
        }

        static double CalculateMatrixMean(double[,] matrix)
        {
            double sum = 0.0;
            int rows = matrix.GetLength(0);
            int cols = matrix.GetLength(1);
            for (int row = 0; row < rows; row++)
                for (int col = 0; col < cols; col++)
                    sum += matrix[row, col];
            return sum / (rows * cols);
        }

        static int CountNonZeroElements(double[,] matrix)
        {
            int count = 0;
            int rows = matrix.GetLength(0);
            int cols = matrix.GetLength(1);
            for (int row = 0; row < rows; row++)
                for (int col = 0; col < cols; col++)
                    if (matrix[row, col] != 0)
                        count++;
            return count;
        }

        static string FlattenMatrix(double[,] matrix, int length)
        {
            string result = string.Empty;
            int rows = matrix.GetLength(0);
            int cols = matrix.GetLength(1);
            for (int i = 0; i < length; i++)
            {
                int row = i / cols;
                int col = i % cols;
                result += (int)Math.Round(matrix[row, col]);
            }
            return result;
        }

        static string BinaryToText(string binary)
        {
            string result = string.Empty;
            for (int i = 0; i < binary.Length; i += 8)
            {
                if (i + 8 > binary.Length) break;
                string byteStr = binary.Substring(i, 8);
                result += (char)Convert.ToInt32(byteStr, 2);
            }
            return result;
        }
    }
}

```


```python
using System;
using MathNet.Numerics.LinearAlgebra;

namespace HarmonicCompressionApp
{
    public class HarmonicCompression
    {
        // Constants for harmonic compression
        private const double HarmonicConstant = 0.35;
        private const double Tolerance = 0.01;
        private const int MaxIterations = 100;

        /// <summary>
        /// Compresses input text using harmonic compression and returns the compressed representation.
        /// </summary>
        public double[,] Compress(string inputText, out string base16Data, out string binaryData, out int originalLength)
        {
            // Step 1: Base-16 encoding
            base16Data = TextToBase16(inputText);

            // Step 2: Convert Base-16 to binary
            binaryData = Base16ToBinary(base16Data);
            originalLength = binaryData.Length;

            // Step 3: Prepare binary matrix
            int matrixSize = (int)Math.Ceiling(Math.Sqrt(originalLength));
            var dataMatrix = CreateBinaryMatrix(binaryData, matrixSize);

            // Step 4: Perform harmonic compression
            return HarmonizeData(dataMatrix, HarmonicConstant, true);
        }

        /// <summary>
        /// Expands a compressed matrix back to the original text.
        /// </summary>
        public string Expand(double[,] compressedMatrix, int originalLength)
        {
            // Step 5: Perform harmonic expansion
            var expandedMatrix = HarmonizeData(compressedMatrix, HarmonicConstant, false);

            // Step 6: Flatten and convert to binary string
            string flattenedBinary = FlattenMatrix(expandedMatrix, originalLength);

            // Step 7: Convert binary back to text
            return BinaryToText(flattenedBinary);
        }

        /// <summary>
        /// Converts input text to its Base-16 representation.
        /// </summary>
        private string TextToBase16(string text)
        {
            char[] chars = text.ToCharArray();
            string result = string.Empty;
            foreach (char c in chars)
                result += Convert.ToString(c, 16).PadLeft(2, '0');
            return result;
        }

        /// <summary>
        /// Converts Base-16 string to binary representation.
        /// </summary>
        private string Base16ToBinary(string base16Data)
        {
            string binary = string.Empty;
            foreach (char c in base16Data)
                binary += Convert.ToString(Convert.ToInt32(c.ToString(), 16), 2).PadLeft(4, '0');
            return binary;
        }

        /// <summary>
        /// Creates a binary matrix from a binary string.
        /// </summary>
        private Matrix<double> CreateBinaryMatrix(string binaryData, int matrixSize)
        {
            var matrix = Matrix<double>.Build.Dense(matrixSize, matrixSize, 0);
            for (int i = 0; i < binaryData.Length; i++)
            {
                int row = i / matrixSize;
                int col = i % matrixSize;
                matrix[row, col] = binaryData[i] == '1' ? 1 : 0;
            }
            return matrix;
        }

        /// <summary>
        /// Harmonizes the data matrix for compression or expansion.
        /// </summary>
        private Matrix<double> HarmonizeData(Matrix<double> data, double harmonicConstant, bool compress)
        {
            var result = data.Clone();
            double gain = compress ? 1.0 : -1.0;

            for (int iteration = 0; iteration < MaxIterations; iteration++)
            {
                double delta = result.RowSums().Average() - harmonicConstant;
                if (Math.Abs(delta) < Tolerance) break;

                result = result.Map(x => Math.Clamp(x - delta * gain, 0.0, 1.0));
            }

            return result;
        }

        /// <summary>
        /// Flattens a matrix back into a binary string.
        /// </summary>
        private string FlattenMatrix(Matrix<double> matrix, int length)
        {
            string result = string.Empty;
            int count = 0;
            foreach (var value in matrix.Enumerate())
            {
                if (count >= length) break;
                result += (int)Math.Round(value);
                count++;
            }
            return result;
        }

        /// <summary>
        /// Converts binary string back to text.
        /// </summary>
        private string BinaryToText(string binary)
        {
            string result = string.Empty;
            for (int i = 0; i < binary.Length; i += 8)
            {
                if (i + 8 > binary.Length) break;
                string byteStr = binary.Substring(i, 8);
                result += (char)Convert.ToInt32(byteStr, 2);
            }
            return result;
        }
    }
}

```


```python
import numpy as np

# Constants
HARMONIC_CONSTANT = 0.35
TOLERANCE = 0.01
MAX_ITERATIONS = 100

# Utility Functions
def text_to_base16(text):
    """Convert text to its base-16 representation."""
    return ''.join(format(ord(char), '02x') for char in text)

def base16_to_text(base16_str):
    """Convert base-16 encoded data back to text."""
    try:
        chars = [chr(int(base16_str[i:i + 2], 16)) for i in range(0, len(base16_str), 2)]
        return ''.join(chars)
    except Exception as e:
        return f"Error decoding base16: {e}"

def binary_to_text(binary_str):
    """Convert binary string back to text."""
    try:
        byte_chunks = [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]
        text = ''.join(chr(int(chunk, 2)) for chunk in byte_chunks if len(chunk) == 8)
        return text
    except Exception as e:
        return f"Error decoding binary: {e}"

# Harmonic Compression and Expansion
def harmonize_data(data, harmonic_constant, compress=True):
    """
    Harmonize data for compression or expansion.
    If compress=True, align data with harmonic resonance for compression.
    If compress=False, expand harmonized data back to its original form.
    """
    data = np.copy(data)
    gain = 1.0 if compress else -1.0

    for _ in range(MAX_ITERATIONS):
        delta = np.mean(data) - harmonic_constant
        adjustment = delta * gain
        data -= adjustment
        data = np.clip(data, 0, 1)  # Ensure binary range
        if abs(delta) < TOLERANCE:
            break

    return data

# Main Framework
def hybrid_storage_to_file(text, filename):
    """Encodes, compresses, writes to file, and reads back for expansion."""
    print("Original Text Length:", len(text))
    print("Original Text:", text[:25])

    # Step 1: Base-16 Encoding
    base16_data = text_to_base16(text)
    print("Base-16 Encoded Data Length:", len(base16_data))
    
    # Step 2: Convert Base-16 Data to Binary
    binary_data = ''.join(format(int(char, 16), '04b') for char in base16_data)
    original_binary_length = len(binary_data)
    print("Binary Data Length:", original_binary_length)

    # Step 3: Prepare Data Matrix
    matrix_size = int(np.ceil(np.sqrt(original_binary_length)))
    data_matrix = np.zeros((matrix_size, matrix_size), dtype=np.float64)
    for i, bit in enumerate(binary_data):
        data_matrix[i // matrix_size, i % matrix_size] = int(bit)

    # Step 4: Harmonic Compression
    compressed_data = harmonize_data(data_matrix, HARMONIC_CONSTANT, compress=True)
    compressed_size = np.count_nonzero(compressed_data)
    print("Compressed Data Non-Zero Elements:", compressed_size)

    # Step 5: Write Compressed Data to File
    np.savez_compressed(filename, compressed_data=compressed_data)
    print(f"Compressed data written to {filename}")

    # Step 6: Read Data Back from File
    loaded_data = np.load(filename)['compressed_data']

    # Step 7: Harmonic Expansion
    expanded_data = harmonize_data(loaded_data, HARMONIC_CONSTANT, compress=False)
    flattened_data = ''.join(str(int(round(bit))) for bit in expanded_data.flatten()[:original_binary_length])

    # Step 8: Convert Binary Back to Text
    recovered_text = binary_to_text(flattened_data)
    print("Recovered Text:", recovered_text[:25])

    # Compression Statistics
    compression_ratio = compressed_size / original_binary_length
    print("Compression Ratio (Compressed/Original):", compression_ratio)

    return recovered_text, compression_ratio

# Example Usage
if __name__ == "__main__":
    # Large Text Dataset
    input_text = "Quantum Storage Test " * 50  # Scaling input text
    filename = "d:\\compressed_data.npz"
    recovered, compression_ratio = hybrid_storage_to_file(input_text, filename)
    print("\nFinal Recovered Text:", recovered[:100])  # Display first 100 characters
    print("Compression Ratio:", compression_ratio)

```

    Original Text Length: 1050
    Original Text: Quantum Storage Test Quan
    Base-16 Encoded Data Length: 2100
    Binary Data Length: 8400
    Compressed Data Non-Zero Elements: 3950
    Compressed data written to d:\compressed_data.npz
    Recovered Text: Quantum Storage Test Quan
    Compression Ratio (Compressed/Original): 0.47023809523809523
    
    Final Recovered Text: Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage Test Quantum Storage 
    Compression Ratio: 0.47023809523809523
    


```python
import wave
import numpy as np
import os

# Constants
HARMONIC_CONSTANT = 0.35
TOLERANCE = 0.01
MAX_ITERATIONS = 100

# 1. Read the WAV File
def read_wav_file(filename):
    """Reads a .wav file and extracts audio data."""
    with wave.open(filename, 'rb') as wav_file:
        n_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        framerate = wav_file.getframerate()
        n_frames = wav_file.getnframes()

        # Extract raw audio data
        raw_data = wav_file.readframes(n_frames)
        
        # Convert bytes to integer data
        dtype = np.int16 if sample_width == 2 else np.int8
        audio_data = np.frombuffer(raw_data, dtype=dtype)
        
        return audio_data, n_channels, sample_width, framerate

# 2. Save WAV File
def save_wav_file(filename, audio_data, n_channels, sample_width, framerate):
    """Saves audio data back to a .wav file."""
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(n_channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(framerate)

        # Convert integer data to bytes and write
        wav_file.writeframes(audio_data.tobytes())

# 3. Convert Audio Data to Binary
def audio_to_binary(audio_data):
    """Converts signed audio data to binary string."""
    max_bits = 16 if audio_data.dtype == np.int16 else 8
    binary_data = ''.join(
        format(sample & (2**max_bits - 1), f'0{max_bits}b') for sample in audio_data
    )
    return binary_data

# 4. Convert Binary Back to Audio
def binary_to_audio(binary_data, dtype):
    """Converts binary string back to signed audio data."""
    max_bits = 16 if dtype == np.int16 else 8
    num_samples = len(binary_data) // max_bits
    audio_data = []

    for i in range(num_samples):
        value = int(binary_data[i * max_bits:(i + 1) * max_bits], 2)
        # Convert from two's complement if necessary
        if value >= 2**(max_bits - 1):
            value -= 2**max_bits
        audio_data.append(value)

    return np.array(audio_data, dtype=dtype)

# 5. Harmonic Compression/Expansion
def harmonize_data(data, harmonic_constant, compress=True):
    """
    Compress or expand data by aligning it with the harmonic constant.
    If compress=True, align data for compression.
    If compress=False, expand compressed data.
    """
    data = np.copy(data)
    gain = 1.0 if compress else -1.0

    for _ in range(MAX_ITERATIONS):
        delta = np.mean(data) - harmonic_constant
        adjustment = delta * gain
        data -= adjustment
        data = np.clip(data, 0, 1)  # Ensure data stays within valid range
        if abs(delta) < TOLERANCE:
            break

    return data

# 6. Compress and Save Data
def compress_audio(audio_data, filename):
    """Compresses audio data, saves it to an .npz file, and returns compression stats."""
    print("Original Audio Length:", len(audio_data))

    # Convert to binary
    binary_data = audio_to_binary(audio_data)
    print("Binary Length:", len(binary_data))

    # Convert binary data to matrix
    binary_length = len(binary_data)
    matrix_size = int(np.ceil(np.sqrt(binary_length)))
    data_matrix = np.zeros((matrix_size, matrix_size), dtype=np.float64)

    # Fill matrix with binary data
    for i, bit in enumerate(binary_data):
        data_matrix[i // matrix_size, i % matrix_size] = int(bit)

    # Harmonic compression
    compressed_data = harmonize_data(data_matrix, HARMONIC_CONSTANT, compress=True)
    print("Compressed Data Non-Zero Elements:", np.count_nonzero(compressed_data))

    # Save compressed data
    np.savez_compressed(filename, compressed_matrix=compressed_data)
    print(f"Compressed data saved to {filename}")

    return compressed_data

# 7. Expand and Restore Audio
def expand_audio(filename, original_dtype):
    """Expands compressed audio data and restores it."""
    # Load compressed data
    loaded_data = np.load(filename)['compressed_matrix']

    # Harmonic expansion
    expanded_data = harmonize_data(loaded_data, HARMONIC_CONSTANT, compress=False)
    
    # Flatten and convert back to binary
    flattened_binary = ''.join(str(int(round(bit))) for bit in expanded_data.flatten())
    
    # Convert binary back to audio data
    restored_audio = binary_to_audio(flattened_binary, original_dtype)
    print("Restored Audio Length:", len(restored_audio))

    return restored_audio

# Main Framework
if __name__ == "__main__":
    # Input and Output Files
    input_wav_file = "d:\\test.wav"
    compressed_file = "d:\\compressed_audio.npz"
    output_wav_file = "d:\\restored.wav"

    # Read the input WAV file
    audio_data, n_channels, sample_width, framerate = read_wav_file(input_wav_file)
    print("Read WAV File:", input_wav_file)

    # Compress and save the audio
    compressed_data = compress_audio(audio_data, compressed_file)

    # Expand and restore the audio
    restored_audio = expand_audio(compressed_file, audio_data.dtype)

    # Save the restored audio back to a new WAV file
    save_wav_file(output_wav_file, restored_audio, n_channels, sample_width, framerate)
    print("Restored WAV File Saved:", output_wav_file)

```

    Read WAV File: d:\test.wav
    Original Audio Length: 20494152
    Binary Length: 327906432
    Compressed Data Non-Zero Elements: 162542701
    Compressed data saved to d:\compressed_audio.npz
    


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    Cell In[23], line 145
        142 compressed_data = compress_audio(audio_data, compressed_file)
        144 # Expand and restore the audio
    --> 145 restored_audio = expand_audio(compressed_file, audio_data.dtype)
        147 # Save the restored audio back to a new WAV file
        148 save_wav_file(output_wav_file, restored_audio, n_channels, sample_width, framerate)
    

    Cell In[23], line 122, in expand_audio(filename, original_dtype)
        119 expanded_data = harmonize_data(loaded_data, HARMONIC_CONSTANT, compress=False)
        121 # Flatten and convert back to binary
    --> 122 flattened_binary = ''.join(str(int(round(bit))) for bit in expanded_data.flatten())
        124 # Convert binary back to audio data
        125 restored_audio = binary_to_audio(flattened_binary, original_dtype)
    

    Cell In[23], line 122, in <genexpr>(.0)
        119 expanded_data = harmonize_data(loaded_data, HARMONIC_CONSTANT, compress=False)
        121 # Flatten and convert back to binary
    --> 122 flattened_binary = ''.join(str(int(round(bit))) for bit in expanded_data.flatten())
        124 # Convert binary back to audio data
        125 restored_audio = binary_to_audio(flattened_binary, original_dtype)
    

    KeyboardInterrupt: 



```python
from tqdm import tqdm
import wave
import numpy as np

# Constants
HARMONIC_CONSTANT = 0.35
TOLERANCE = 0.01
MAX_ITERATIONS = 100

# 1. Read WAV File
def read_wav_file(filename):
    """Reads a .wav file and extracts audio data."""
    with wave.open(filename, 'rb') as wav_file:
        n_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        framerate = wav_file.getframerate()
        n_frames = wav_file.getnframes()

        # Extract raw audio data
        raw_data = wav_file.readframes(n_frames)
        
        # Convert bytes to integer data
        dtype = np.int16 if sample_width == 2 else np.int8
        audio_data = np.frombuffer(raw_data, dtype=dtype)
        
        return audio_data, n_channels, sample_width, framerate

# 2. Save WAV File
def save_wav_file(filename, audio_data, n_channels, sample_width, framerate):
    """Saves audio data back to a .wav file."""
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(n_channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(framerate)

        # Convert integer data to bytes and write
        wav_file.writeframes(audio_data.tobytes())

# 3. Convert Audio to Binary with Progress Meter
def audio_to_binary(audio_data):
    """Converts signed audio data to binary string with progress tracking."""
    max_bits = 16 if audio_data.dtype == np.int16 else 8
    binary_data = ''.join(
        format(sample & (2**max_bits - 1), f'0{max_bits}b') 
        for sample in tqdm(audio_data, desc="Converting audio to binary")
    )
    return binary_data

# 4. Convert Binary to Matrix with Progress Meter
def binary_to_matrix(binary_data):
    """Converts binary data to a 2D matrix with progress tracking."""
    binary_length = len(binary_data)
    matrix_size = int(np.ceil(np.sqrt(binary_length)))
    data_matrix = np.zeros((matrix_size, matrix_size), dtype=np.float64)

    for i, bit in tqdm(enumerate(binary_data), total=binary_length, desc="Filling matrix"):
        data_matrix[i // matrix_size, i % matrix_size] = int(bit)

    return data_matrix

# 5. Harmonize Data with Progress Meter
def harmonize_data(data, harmonic_constant, compress=True):
    """Compress or expand data by aligning it with the harmonic constant, with progress tracking."""
    data = np.copy(data)
    gain = 1.0 if compress else -1.0

    for iteration in tqdm(range(MAX_ITERATIONS), desc="Harmonic adjustment"):
        delta = np.mean(data) - harmonic_constant
        adjustment = delta * gain
        data -= adjustment
        data = np.clip(data, 0, 1)  # Ensure binary range
        if abs(delta) < TOLERANCE:
            break

    return data

# 6. Binary to Audio
def binary_to_audio(binary_data, dtype):
    """Converts binary string back to signed audio data."""
    max_bits = 16 if dtype == np.int16 else 8
    num_samples = len(binary_data) // max_bits
    audio_data = []

    for i in range(num_samples):
        value = int(binary_data[i * max_bits:(i + 1) * max_bits], 2)
        # Convert from two's complement if necessary
        if value >= 2**(max_bits - 1):
            value -= 2**max_bits
        audio_data.append(value)

    return np.array(audio_data, dtype=dtype)

# Main Workflow
if __name__ == "__main__":
    # Input and Output Files
    input_wav_file = "d:\\test.wav"
    compressed_file = "d:\\compressed_audio.npz"
    output_wav_file = "d:\\restored.wav"

    # Step 1: Read the Input WAV File
    audio_data, n_channels, sample_width, framerate = read_wav_file(input_wav_file)
    print(f"Read WAV File: {input_wav_file}")
    print(f"Channels: {n_channels}, Sample Width: {sample_width}, Frame Rate: {framerate}")

    # Step 2: Convert Audio to Binary
    binary_data = audio_to_binary(audio_data)

    # Step 3: Convert Binary to Matrix
    data_matrix = binary_to_matrix(binary_data)

    # Step 4: Apply Harmonic Compression
    compressed_data = harmonize_data(data_matrix, HARMONIC_CONSTANT, compress=True)
    print("Compressed Data Non-Zero Elements:", np.count_nonzero(compressed_data))

    # Step 5: Save Compressed Data
    np.savez_compressed(compressed_file, compressed_matrix=compressed_data)
    print(f"Compressed data saved to {compressed_file}")

    # Step 6: Load Compressed Data and Expand
    loaded_data = np.load(compressed_file)['compressed_matrix']
    expanded_data = harmonize_data(loaded_data, HARMONIC_CONSTANT, compress=False)

    # Step 7: Flatten Expanded Data and Convert Back to Audio
    flattened_binary = ''.join(str(int(round(bit))) for bit in tqdm(expanded_data.flatten(), desc="Flattening matrix"))
    restored_audio = binary_to_audio(flattened_binary, audio_data.dtype)

    # Step 8: Save Restored Audio to a New WAV File
    save_wav_file(output_wav_file, restored_audio, n_channels, sample_width, framerate)
    print(f"Restored WAV File Saved: {output_wav_file}")

```

    Read WAV File: d:\test.wav
    Channels: 2, Sample Width: 2, Frame Rate: 44100
    

    Converting audio to binary: 100%|██████████| 20494152/20494152 [01:26<00:00, 237924.64it/s]
    Filling matrix: 100%|██████████| 327906432/327906432 [02:30<00:00, 2179190.31it/s]
    Harmonic adjustment:   4%|▍         | 4/100 [00:08<03:12,  2.00s/it]
    

    Compressed Data Non-Zero Elements: 162542701
    Compressed data saved to d:\compressed_audio.npz
    

    Harmonic adjustment:   0%|          | 0/100 [00:01<?, ?it/s]
    Flattening matrix: 100%|██████████| 327935881/327935881 [13:37<00:00, 401304.51it/s]
    

    Restored WAV File Saved: d:\restored.wav
    


```python
from tqdm import tqdm
import wave
import numpy as np

# Constants
HARMONIC_CONSTANT = 0.35
TOLERANCE = 0.01
MAX_ITERATIONS = 100

# 1. Read WAV File
def read_wav_file(filename):
    """Reads a .wav file and extracts audio data."""
    with wave.open(filename, 'rb') as wav_file:
        n_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        framerate = wav_file.getframerate()
        n_frames = wav_file.getnframes()

        # Extract raw audio data
        raw_data = wav_file.readframes(n_frames)
        
        # Convert bytes to integer data
        dtype = np.int16 if sample_width == 2 else np.int8
        audio_data = np.frombuffer(raw_data, dtype=dtype)
        
        return audio_data, n_channels, sample_width, framerate

# 2. Save WAV File
def save_wav_file(filename, audio_data, n_channels, sample_width, framerate):
    """Saves audio data back to a .wav file."""
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(n_channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(framerate)

        # Convert integer data to bytes and write
        wav_file.writeframes(audio_data.tobytes())

# 3. Convert Audio to Binary with Progress Meter
def audio_to_binary(audio_data):
    """Converts signed audio data to binary string with progress tracking."""
    max_bits = 16 if audio_data.dtype == np.int16 else 8
    binary_data = ''.join(
        format(sample & (2**max_bits - 1), f'0{max_bits}b') 
        for sample in tqdm(audio_data, desc="Converting audio to binary")
    )
    return binary_data

# 4. Convert Binary to Matrix with Progress Meter
def binary_to_matrix(binary_data):
    """Converts binary data to a 2D matrix with progress tracking."""
    binary_length = len(binary_data)
    matrix_size = int(np.ceil(np.sqrt(binary_length)))
    data_matrix = np.zeros((matrix_size, matrix_size), dtype=np.float64)

    for i, bit in tqdm(enumerate(binary_data), total=binary_length, desc="Filling matrix"):
        data_matrix[i // matrix_size, i % matrix_size] = int(bit)

    return data_matrix

# 5. Harmonize Data with Progress Meter
def harmonize_data(data, harmonic_constant, compress=True):
    """Compress or expand data by aligning it with the harmonic constant, with progress tracking."""
    data = np.copy(data)
    gain = 1.0 if compress else -1.0

    for iteration in tqdm(range(MAX_ITERATIONS), desc="Harmonic adjustment"):
        delta = np.mean(data) - harmonic_constant
        adjustment = delta * gain
        data -= adjustment
        data = np.clip(data, 0, 1)  # Ensure binary range
        if abs(delta) < TOLERANCE:
            break

    return data

# 6. Binary to Audio
def binary_to_audio(binary_data, dtype):
    """Converts binary string back to signed audio data."""
    max_bits = 16 if dtype == np.int16 else 8
    num_samples = len(binary_data) // max_bits
    audio_data = []

    for i in range(num_samples):
        value = int(binary_data[i * max_bits:(i + 1) * max_bits], 2)
        # Convert from two's complement if necessary
        if value >= 2**(max_bits - 1):
            value -= 2**max_bits
        audio_data.append(value)

    return np.array(audio_data, dtype=dtype)

# Main Workflow
if __name__ == "__main__":
    # Input and Output Files
    input_wav_file = "d:\\test.wav"
    compressed_file = "d:\\compressed_audio.npz"
    output_wav_file = "d:\\restored.wav"

    # Step 1: Read the Input WAV File
    audio_data, n_channels, sample_width, framerate = read_wav_file(input_wav_file)
    print(f"Read WAV File: {input_wav_file}")
    print(f"Channels: {n_channels}, Sample Width: {sample_width}, Frame Rate: {framerate}")

    # Step 2: Convert Audio to Binary
    binary_data = audio_to_binary(audio_data)

    # Step 3: Convert Binary to Matrix
    data_matrix = binary_to_matrix(binary_data)

    # Step 4: Apply Harmonic Compression
    compressed_data = harmonize_data(data_matrix, HARMONIC_CONSTANT, compress=True)
    print("Compressed Data Non-Zero Elements:", np.count_nonzero(compressed_data))

    # Step 5: Save Compressed Data
    np.savez_compressed(compressed_file, compressed_matrix=compressed_data)
    print(f"Compressed data saved to {compressed_file}")

    # Step 6: Load Compressed Data and Expand
    loaded_data = np.load(compressed_file)['compressed_matrix']
    expanded_data = harmonize_data(loaded_data, HARMONIC_CONSTANT, compress=False)

    # Step 7: Flatten Expanded Data and Convert Back to Audio
    flattened_binary = ''.join(str(int(round(bit))) for bit in tqdm(expanded_data.flatten(), desc="Flattening matrix"))
    restored_audio = binary_to_audio(flattened_binary, audio_data.dtype)

    # Step 8: Save Restored Audio to a New WAV File
    save_wav_file(output_wav_file, restored_audio, n_channels, sample_width, framerate)
    print(f"Restored WAV File Saved: {output_wav_file}")

```

    Read WAV File: d:\test.wav
    Channels: 2, Sample Width: 2, Frame Rate: 44100
    

    Converting audio to binary: 100%|██████████| 20494152/20494152 [01:24<00:00, 241225.28it/s]
    Filling matrix: 100%|██████████| 327906432/327906432 [02:33<00:00, 2139701.71it/s]
    Harmonic adjustment:   4%|▍         | 4/100 [00:08<03:20,  2.09s/it]
    

    Compressed Data Non-Zero Elements: 162542701
    Compressed data saved to d:\compressed_audio.npz
    

    Harmonic adjustment:   0%|          | 0/100 [00:01<?, ?it/s]
    Flattening matrix: 100%|██████████| 327935881/327935881 [13:37<00:00, 400995.08it/s]
    

    Restored WAV File Saved: d:\restored.wav
    


```python
from tqdm import tqdm
import numpy as np

# Constants
HARMONIC_CONSTANT = 0.35
TOLERANCE = 0.01
MAX_ITERATIONS = 100

# 1. Read File as Raw Bytes
def read_file_as_bytes(filename):
    """Reads a file as raw bytes."""
    with open(filename, 'rb') as f:
        raw_data = f.read()
    print(f"File size: {len(raw_data)} bytes")
    return raw_data

# 2. Save File from Raw Bytes
def save_file_from_bytes(filename, raw_bytes):
    """Writes raw bytes to a file."""
    with open(filename, 'wb') as f:
        f.write(raw_bytes)
    print(f"File saved: {filename}, Size: {len(raw_bytes)} bytes")

# 3. Convert Bytes to Matrix
def bytes_to_matrix(raw_data):
    """Converts raw bytes into a 2D matrix."""
    binary_length = len(raw_data) * 8  # Total bits
    matrix_size = int(np.ceil(np.sqrt(binary_length)))  # Square matrix size
    data_matrix = np.zeros((matrix_size, matrix_size), dtype=np.float64)

    # Fill the matrix with binary data
    for i in tqdm(range(len(raw_data)), desc="Converting bytes to matrix"):
        byte = raw_data[i]
        for bit_index in range(8):
            bit = (byte >> (7 - bit_index)) & 1
            index = i * 8 + bit_index
            if index < binary_length:
                row = index // matrix_size
                col = index % matrix_size
                data_matrix[row, col] = bit

    return data_matrix, binary_length

# 4. Convert Matrix Back to Bytes
def matrix_to_bytes(expanded_matrix, original_length):
    """Converts a 2D matrix back into raw bytes."""
    flat_bits = []
    for row in expanded_matrix:
        for bit in row:
            flat_bits.append(int(round(bit)))

    # Trim to original bit length
    flat_bits = flat_bits[:original_length]
    raw_bytes = bytearray()

    # Group bits into bytes
    for i in range(0, len(flat_bits), 8):
        byte = 0
        for bit_index in range(8):
            if i + bit_index < len(flat_bits):
                byte |= flat_bits[i + bit_index] << (7 - bit_index)
        raw_bytes.append(byte)

    return bytes(raw_bytes)

# 5. Harmonize Data (Compression/Expansion)
def harmonize_data(data, harmonic_constant, compress=True):
    """Compress or expand data by aligning with the harmonic constant."""
    data = np.copy(data)
    gain = 1.0 if compress else -1.0

    for iteration in tqdm(range(MAX_ITERATIONS), desc="Harmonic adjustment"):
        delta = np.mean(data) - harmonic_constant
        adjustment = delta * gain
        data -= adjustment
        data = np.clip(data, 0, 1)  # Ensure values stay in binary range
        if abs(delta) < TOLERANCE:
            break

    return data

# Main Workflow
if __name__ == "__main__":
    # Input and Output Files
    input_file = "d:\\test.wav"  # Can be any file, not just .wav
    compressed_file = "d:\\compressed_data.npz"
    output_file = "d:\\restored_output.wav"

    # Step 1: Read Input File as Bytes
    raw_data = read_file_as_bytes(input_file)

    # Step 2: Convert Bytes to Matrix
    data_matrix, binary_length = bytes_to_matrix(raw_data)

    # Step 3: Apply Harmonic Compression
    compressed_data = harmonize_data(data_matrix, HARMONIC_CONSTANT, compress=True)
    print(f"Compressed Data Non-Zero Elements: {np.count_nonzero(compressed_data)}")

    # Step 4: Save Compressed Data
    np.savez_compressed(compressed_file, compressed_matrix=compressed_data)
    print(f"Compressed data saved to {compressed_file}")

    # Step 5: Load Compressed Data and Expand
    loaded_data = np.load(compressed_file)['compressed_matrix']
    expanded_data = harmonize_data(loaded_data, HARMONIC_CONSTANT, compress=False)

    # Step 6: Convert Matrix Back to Bytes
    restored_bytes = matrix_to_bytes(expanded_data, binary_length)

    # Step 7: Save Restored File
    save_file_from_bytes(output_file, restored_bytes)

```

    File size: 41104732 bytes
    

    Converting bytes to matrix: 100%|██████████| 41104732/41104732 [01:40<00:00, 410956.51it/s]
    Harmonic adjustment:   4%|▍         | 4/100 [00:08<03:14,  2.02s/it]
    

    Compressed Data Non-Zero Elements: 163001414
    Compressed data saved to d:\compressed_data.npz
    

    Harmonic adjustment:   0%|          | 0/100 [00:01<?, ?it/s]
    

    File saved: d:\restored_output.wav, Size: 41104732 bytes
    


```python
from tqdm import tqdm
import numpy as np
from scipy.fft import rfft, irfft

# Constants
HARMONIC_CONSTANT = 0.35
TOLERANCE = 0.01
MAX_ITERATIONS = 100

# 1. Read File as Bytes
def read_file_as_bytes(filename):
    """Reads a file as raw bytes."""
    with open(filename, 'rb') as f:
        raw_data = f.read()
    print(f"File size: {len(raw_data)} bytes")
    return raw_data

# 2. Difference Encoding
def difference_encode(audio_data):
    """Encodes differences between consecutive samples."""
    return np.diff(audio_data, prepend=audio_data[0])

def difference_decode(encoded_data):
    """Decodes difference-encoded data back to original form."""
    return np.cumsum(encoded_data)

# 3. Sparse Encoding
def sparse_encode(audio_data):
    """Encodes sparse data by storing non-zero values and their indices."""
    indices = np.nonzero(audio_data)[0]
    values = audio_data[indices]
    return indices, values

def sparse_decode(indices, values, original_length):
    """Decodes sparse data back to the original form."""
    decoded = np.zeros(original_length, dtype=values.dtype)
    decoded[indices] = values
    return decoded

# 4. Fourier Transform Compression
def harmonic_compress(audio_data):
    """Compress audio data using Fourier Transform."""
    transformed = rfft(audio_data)  # Real-to-complex Fourier Transform
    return transformed

def harmonic_expand(compressed_data):
    """Expand compressed data using Inverse Fourier Transform."""
    restored = irfft(compressed_data)
    return np.round(restored).astype(np.int16)  # Round to integers

# Main Workflow
if __name__ == "__main__":
    # Input and Output Files
    input_file = "d:\\test.wav"  # Can be any file, not just .wav
    compressed_file = "d:\\compressed_data.npz"
    output_file = "d:\\restored_output.wav"

    # Step 1: Read Input File as Bytes
    raw_data = read_file_as_bytes(input_file)

    # Step 2: Difference Encode
    encoded_diff = difference_encode(raw_data)

    # Step 3: Apply Fourier Transform Compression
    compressed_data = harmonic_compress(encoded_diff)

    # Save Compressed Data
    np.savez_compressed(compressed_file, compressed_data=compressed_data)
    print(f"Compressed data saved to {compressed_file}")

    # Load and Expand
    loaded_data = np.load(compressed_file)['compressed_data']
    expanded_diff = harmonic_expand(loaded_data)

    # Step 4: Decode Differences
    restored_data = difference_decode(expanded_diff)

    # Step 5: Save Restored File
    save_file_from_bytes(output_file, restored_data)

```

    File size: 41104732 bytes
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[31], line 62
         59 raw_data = read_file_as_bytes(input_file)
         61 # Step 2: Difference Encode
    ---> 62 encoded_diff = difference_encode(raw_data)
         64 # Step 3: Apply Fourier Transform Compression
         65 compressed_data = harmonic_compress(encoded_diff)
    

    Cell In[31], line 21, in difference_encode(audio_data)
         19 def difference_encode(audio_data):
         20     """Encodes differences between consecutive samples."""
    ---> 21     return np.diff(audio_data, prepend=audio_data[0])
    

    File ~\anaconda3\Lib\site-packages\numpy\lib\function_base.py:1418, in diff(a, n, axis, prepend, append)
       1416 nd = a.ndim
       1417 if nd == 0:
    -> 1418     raise ValueError("diff requires input that is at least one dimensional")
       1419 axis = normalize_axis_index(axis, nd)
       1421 combined = []
    

    ValueError: diff requires input that is at least one dimensional



```python

```
