# jsoncons v1.1.0 Release Notes

**Release Date:** January 4, 2026

## 🎉 Overview

`jsoncons` v1.1.0 introduces **Fibonacci Hashing Integration**, a powerful multiplicative hashing technique for efficient hash table indexing. This release adds new CLI commands, a comprehensive Fibonacci hashing function, and an educational Jupyter Notebook demonstrating performance benefits. All existing functionality remains fully backward compatible.

---

## ✨ New Features

### 1. **Fibonacci Hashing Function**

A new `fibonacci_hash_to_index()` function provides efficient mapping of 64-bit hash values to indices in power-of-2 sized hash tables.

**Key Benefits:**
- ⚡ **Performance**: Uses only multiplication and bit-shift operations (faster than modulo hashing)
- 📊 **Distribution**: Uniform distribution across hash table indices using the golden ratio
- 🔧 **Extensible**: Foundation for future performance optimizations in internal data structures

**Usage:**
```python
from jsoncons.cli import fibonacci_hash_to_index

# Map a hash value to a table index
index = fibonacci_hash_to_index(hash_value=12345, table_size_power_of_2=1024)
print(f"Hash index: {index}")  # Output: 0-1023
```

**Technical Details:**
- Uses the magic constant `11400714819323198485` (derived from 2^64 / φ, where φ is the golden ratio)
- Requires power-of-2 table sizes for optimal performance
- Raises `ValueError` for invalid inputs (non-power-of-2 sizes, zero, or negative values)

---

### 2. **New CLI Commands**

#### `process_json_fib`
Fibonacci variant of JSON validation and formatting. Functionally identical to `encode`/`decode` with consistent command naming patterns.

```bash
# Process JSON with Fibonacci variant
jsoncons process_json_fib input.json output.json

# With formatting options
jsoncons process_json_fib --indent 4 --sort-keys input.json output.json
```

#### `cobol_to_json_fib`
Fibonacci variant of COBOL-to-JSON conversion. Uses the new `parse_cobol_line_fib` parser while maintaining identical output to the original command.

```bash
# Convert COBOL to JSON with Fibonacci variant
jsoncons cobol_to_json_fib --layout-file layout.json input.cobol output.json
```

---

### 3. **Comprehensive Jupyter Notebook Demo**

A new `Fibonacci_Hashing_Demo.ipynb` notebook provides hands-on demonstrations of Fibonacci hashing principles:

**Included Demonstrations:**
- 📊 **Performance Benchmarks**: Compares Fibonacci, modulo, and bitwise AND hashing with 100,000+ operations
- 📈 **Distribution Analysis**: Histograms showing uniform distribution across hash table indices
- 🎓 **Step-by-Step Visualization**: Visual breakdown of the Fibonacci hashing algorithm
- 🔬 **Educational Content**: Learn advanced hashing techniques with practical examples
- 💡 **Practical Applications**: Real-world use cases and optimization strategies

**Running the Notebook:**
```bash
jupyter notebook Fibonacci_Hashing_Demo.ipynb
```

---

## 🔄 Backward Compatibility

✅ **All existing commands work unchanged:**
- `encode` - Validate and pretty-print JSON
- `decode` - Alias for encode
- `cobol_to_json` - Convert COBOL data to JSON

No breaking changes. Existing workflows continue to function identically.

---

## 🐛 Bug Fixes

- Fixed f-string compatibility issue in COBOL-to-JSON function (v1.0.4)
- Improved error handling for short COBOL records with proper padding and warnings

---

## 📋 What is Fibonacci Hashing?

Fibonacci hashing is a multiplicative hashing technique that uses the golden ratio to distribute hash values uniformly across power-of-2 sized hash tables. It's particularly effective for:

- **Hash table implementations** where you need to map pre-computed hash values to table indices
- **Performance-critical applications** requiring faster hashing than modulo operations
- **Uniform distribution** of hash values across the available range

**Why It Matters:**
- Faster than integer modulo for arbitrary table sizes
- Comparable speed to bitwise AND for power-of-2 sizes
- Better distribution than simple bitwise AND operations
- Mixes bits effectively, spreading patterned inputs evenly

---

## 🧪 Testing & Quality

- ✅ Comprehensive unit tests for all new functions
- ✅ Property-based tests verifying consistency and distribution
- ✅ Tested on Python 3.8+, 3.11.1, 3.11.2, 3.12.1
- ✅ Full backward compatibility verification

---

## 📦 Installation

```bash
pip install jsoncons==1.1.0
```

Or upgrade from a previous version:
```bash
pip install --upgrade jsoncons
```

---

## 🚀 Roadmap to v2.0.0

- Integration with IBM zOS
- Performance optimizations using Fibonacci hashing in internal data structures
- Enhanced COBOL field lookup with hash table acceleration
- Extended support for additional COBOL data types

---

## 📝 Documentation

- **README.md** - General usage and feature overview
- **README-fib.md** - Detailed Fibonacci hashing implementation guide
- **Fibonacci_Hashing_Demo.ipynb** - Interactive demonstrations and benchmarks

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Open an issue to discuss your change
2. Fork the repository
3. Create a new branch (`git checkout -b feature/your-feature-name`)
4. Make your changes and commit them
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

Fibonacci hashing implementation based on established multiplicative hashing techniques using the golden ratio constant. Special thanks to the community for feedback and contributions.

---

## 📞 Support

For issues, questions, or feature requests, please visit the [GitHub repository](https://github.com/your-org/jsoncons) or open an issue.

---

**Happy hashing! 🎉**
