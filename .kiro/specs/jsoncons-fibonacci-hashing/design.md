# Design Document: jsoncons v1.0.5 - Fibonacci Hashing Integration

## Overview

This design document outlines the implementation of Fibonacci hashing capabilities in the jsoncons package. The feature adds new CLI commands and functions that demonstrate Fibonacci hashing principles while maintaining full backward compatibility with existing functionality. The implementation includes:

1. A `fibonacci_hash_to_index()` function that maps 64-bit hash values to indices in power-of-2 sized hash tables
2. Fibonacci variant functions for COBOL parsing and JSON processing (`parse_cobol_line_fib`, `process_cobol_to_json_fib`, `process_json_fib`)
3. Corresponding CLI commands that expose these functions
4. A comprehensive Jupyter Notebook demonstrating Fibonacci hashing performance and distribution characteristics
5. Full test coverage including unit tests and property-based tests

## Architecture

The architecture maintains a layered approach:

```
┌─────────────────────────────────────────────────────────────┐
│                    CLI Layer (argparse)                      │
│  encode | decode | cobol_to_json | process_json_fib | ...   │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│              Processing Functions Layer                      │
│  process_json() | process_cobol_to_json()                   │
│  process_json_fib() | process_cobol_to_json_fib()           │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│              Parsing & Hashing Functions Layer               │
│  parse_cobol_line() | parse_cobol_line_fib()                │
│  fibonacci_hash_to_index()                                   │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│                  Utility & Helper Layer                      │
│  CobolParsingError | DecimalEncoder | Logging               │
└─────────────────────────────────────────────────────────────┘
```

## Components and Interfaces

### 1. Fibonacci Hashing Component

**Module:** `jsoncons.cli`

**Function Signature:**
```python
def fibonacci_hash_to_index(hash_value: int, table_size_power_of_2: int) -> int
```

**Purpose:** Maps a 64-bit hash value to an index for a power-of-2 sized hash table using Fibonacci hashing.

**Parameters:**
- `hash_value` (int): The input hash value (treated as 64-bit)
- `table_size_power_of_2` (int): The size of the hash table (must be a power of 2)

**Returns:** An integer index in the range [0, table_size_power_of_2 - 1]

**Raises:** ValueError if table_size_power_of_2 is not a positive power of 2

**Implementation Details:**
- Uses the magic constant: `FIB_HASH_64_MAGIC = 11400714819323198485` (approximately 2^64 / φ)
- Performs 64-bit multiplication with wraparound
- Extracts the high-order bits via right shift
- Shift amount calculated as: `64 - (table_size_power_of_2.bit_length() - 1)`

### 2. COBOL Parsing Component

**Existing Function:** `parse_cobol_line(line, layout_config, line_num)`

**New Variant Function:** `parse_cobol_line_fib(line, layout_config, line_num)`

**Purpose:** Parse a single line of fixed-width COBOL data according to a layout specification.

**Behavior:**
- `parse_cobol_line_fib` delegates to `parse_cobol_line` for actual parsing logic
- Maintains identical behavior to the original function
- Supports PIC X (alphanumeric), PIC 9 (numeric), and PIC S9 (signed numeric) types
- Handles implied decimals for numeric fields
- Logs warnings for data length mismatches
- Raises `CobolParsingError` for parsing failures

### 3. COBOL-to-JSON Processing Component

**Existing Function:** `process_cobol_to_json(layout_file, infile, outfile)`

**New Variant Function:** `process_cobol_to_json_fib(layout_file, infile, outfile)`

**Purpose:** Convert fixed-width COBOL data to JSON format.

**Behavior:**
- Loads layout configuration from JSON file
- Iterates through input lines, parsing each with the appropriate parser
- Skips empty lines and lines with parsing errors
- Outputs valid JSON with proper formatting
- Uses `DecimalEncoder` to preserve numeric precision
- Logs informational and error messages to stderr

### 4. JSON Processing Component

**Existing Function:** `process_json(infile, outfile, indent=2, sort_keys=False)`

**New Variant Function:** `process_json_fib(infile, outfile, indent=2, sort_keys=False)`

**Purpose:** Validate and format JSON data.

**Behavior:**
- `process_json_fib` delegates to `process_json` for actual processing
- Reads JSON from input, validates it, and writes formatted output
- Supports custom indentation levels
- Optionally sorts keys in output
- Handles encoding with `ensure_ascii=False` for Unicode support

### 5. CLI Command Interface

**New Commands:**
- `process_json_fib`: Alias for encode/decode with Fibonacci naming convention
- `cobol_to_json_fib`: COBOL-to-JSON conversion using Fibonacci variant parser

**Command Structure:**
```
jsoncons process_json_fib [--indent N] [--sort-keys] [infile] [outfile]
jsoncons cobol_to_json_fib --layout-file LAYOUT [infile] [outfile]
```

## Data Models

### COBOL Layout Configuration

```json
{
  "record_length": 80,
  "fields": [
    {
      "name": "field_name",
      "start_pos": 1,
      "length": 10,
      "type": "PIC X",
      "strip": false,
      "decimals": 0,
      "signed": false
    }
  ]
}
```

### Parsed Record Output

```json
{
  "field_name": "value",
  "numeric_field": 12345,
  "decimal_field": "123.45"
}
```

### Error Handling Data

```python
class CobolParsingError(ValueError):
    """Custom error for COBOL parsing issues."""
    pass
```

## Correctness Properties

A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.

### Property 1: Fibonacci Hash Index Range Validity

*For any* valid 64-bit hash value and power-of-2 table size, the returned index SHALL be within the valid range [0, table_size - 1].

**Validates: Requirements 1.1**

### Property 2: Fibonacci Hash Consistency

*For any* hash value and table size, calling `fibonacci_hash_to_index` multiple times with the same inputs SHALL return the identical index.

**Validates: Requirements 1.5**

### Property 3: Fibonacci Hash Distribution Uniformity

*For any* set of distinct hash values and a power-of-2 table size, the distribution of resulting indices across the available range SHALL be approximately uniform (no significant clustering).

**Validates: Requirements 1.4**

### Property 4: COBOL Parsing Equivalence

*For any* valid COBOL data line and layout configuration, `parse_cobol_line_fib` SHALL produce identical output to `parse_cobol_line`.

**Validates: Requirements 2.1**

### Property 5: COBOL-to-JSON Conversion Equivalence

*For any* valid COBOL data file and layout configuration, `process_cobol_to_json_fib` SHALL produce identical JSON output to `process_cobol_to_json`.

**Validates: Requirements 3.2**

### Property 6: JSON Processing Equivalence

*For any* valid JSON input, `process_json_fib` SHALL produce identical formatted output to `process_json`.

**Validates: Requirements 4.1**

### Property 7: Fibonacci Hash Error Handling

*For any* invalid table size (non-power-of-2 or non-positive), `fibonacci_hash_to_index` SHALL raise a ValueError with a descriptive message.

**Validates: Requirements 1.2, 1.3**

### Property 8: COBOL Parsing Error Handling

*For any* invalid COBOL data that violates the layout specification, `parse_cobol_line_fib` SHALL raise a CobolParsingError with contextual information.

**Validates: Requirements 2.2**

### Property 9: JSON Validation Round-Trip

*For any* valid JSON input, parsing and then formatting SHALL produce valid JSON that can be parsed again without errors.

**Validates: Requirements 4.4**

## Error Handling

### Fibonacci Hashing Errors

- **Invalid Table Size:** Raises `ValueError` if table_size_power_of_2 is not a positive power of 2
- **Overflow Handling:** Uses 64-bit masking to handle wraparound in multiplication

### COBOL Parsing Errors

- **CobolParsingError:** Raised for field conversion failures with line number and field context
- **Length Mismatch:** Logged as warning; processing continues with padding
- **Invalid Numeric Values:** Caught and reported with field-specific context

### JSON Processing Errors

- **JSONDecodeError:** Caught and reported with input source identification
- **File I/O Errors:** Caught and reported with file path context
- **Same Input/Output File:** Detected and prevented with clear error message

### Logging Strategy

- **INFO Level:** Successful operations and completion messages
- **WARNING Level:** Data length mismatches, skipped lines
- **ERROR Level:** Parsing failures, file not found, invalid JSON
- **Output:** All logging directed to stderr to keep stdout clean for data output

## Testing Strategy

### Unit Testing Approach

Unit tests verify specific examples and edge cases:

1. **Fibonacci Hash Function Tests:**
   - Valid inputs with various table sizes (8, 16, 1024, etc.)
   - Edge cases (hash value 0, maximum 64-bit value)
   - Invalid table sizes (non-power-of-2, zero, negative)
   - Consistency across multiple calls

2. **COBOL Parsing Tests:**
   - Valid records with various field types
   - Records with implied decimals
   - Records with signed numeric fields
   - Short records (padding behavior)
   - Invalid numeric values (error handling)

3. **JSON Processing Tests:**
   - Valid JSON with various structures
   - Invalid JSON (error handling)
   - Indentation options (0, 2, 4)
   - Sort keys option
   - Unicode handling

4. **CLI Integration Tests:**
   - Command execution with file I/O
   - stdin/stdout handling
   - Error conditions and exit codes
   - Same input/output file detection

### Property-Based Testing Approach

Property-based tests verify universal properties across generated inputs using **Hypothesis** (Python's property-based testing library):

1. **Fibonacci Hash Properties:**
   - For all valid hash values and power-of-2 sizes: index is in valid range
   - For all identical inputs: output is consistent
   - For all distinct hash values: distribution is uniform

2. **Parsing Equivalence Properties:**
   - For all valid COBOL data: `_fib` variant produces identical output
   - For all valid JSON: `_fib` variant produces identical output

3. **Error Handling Properties:**
   - For all invalid table sizes: ValueError is raised
   - For all invalid JSON: JSONDecodeError is caught and reported

### Test Configuration

- **Minimum Iterations:** 100 per property-based test
- **Test Framework:** unittest for unit tests, Hypothesis for property-based tests
- **Test Location:** `tests/test_cli.py` for CLI tests, `tests/test_fibonacci_hashing.py` for Fibonacci-specific tests
- **Coverage Target:** Minimum 90% code coverage for new functions

### Jupyter Notebook Testing

The demonstration notebook includes:

1. **Data Generation:** Creates sample COBOL data using jsoncons
2. **Performance Benchmarking:** Measures execution time for three hashing methods
3. **Distribution Analysis:** Visualizes index distribution via histograms
4. **Visualization Cell:** Step-by-step demonstration of Fibonacci hashing operation
5. **Cleanup:** Removes temporary files after execution

## Hash Function Selection and Optimization

### Current Approach: Python's Built-in `hash()`

The demonstration notebook uses Python's built-in `hash()` function to generate initial hash values for the Fibonacci hashing demonstration. This approach:
- Is portable across platforms
- Requires no external dependencies
- Is suitable for demonstration purposes
- Provides adequate distribution for the notebook's educational goals

### Optional Optimization: MurmurHash

**Consideration:** MurmurHash is a non-cryptographic hash function known for excellent distribution and performance characteristics. It could be used to generate initial hash values for the Fibonacci hashing demonstration.

**Decision:** MurmurHash integration is marked as optional for v1.0.5:
- **Rationale:** The core Fibonacci hashing functionality does not require MurmurHash; it works with any 64-bit hash input
- **Security:** MurmurHash is non-cryptographic and suitable for hash table applications (not for security-sensitive operations)
- **Implementation:** If included, would be via the `mmh3` package (optional dependency)
- **Benefit:** Could improve distribution demonstration in the notebook
- **Trade-off:** Adds external dependency; Python's built-in `hash()` is sufficient for v1.0.5

**Future Enhancement:** MurmurHash integration can be added in v1.1.0 as an optional feature for users who want to demonstrate Fibonacci hashing with a well-known, battle-tested hash function.

## Implementation Phases

### Phase 1: Core Fibonacci Hashing Function
- Implement `fibonacci_hash_to_index()` with full validation
- Add unit tests for the function
- Add property-based tests for distribution and consistency

### Phase 2: Variant Functions
- Implement `parse_cobol_line_fib()` as delegation to original
- Implement `process_cobol_to_json_fib()` with identical behavior
- Implement `process_json_fib()` as delegation to original
- Add unit tests for equivalence

### Phase 3: CLI Integration
- Add `process_json_fib` subcommand
- Add `cobol_to_json_fib` subcommand
- Add CLI integration tests

### Phase 4: Demonstration Notebook
- Create Jupyter Notebook with performance benchmarks
- Add distribution analysis visualizations
- Add step-by-step Fibonacci hashing visualization
- Include cleanup and conclusions
- Use Python's built-in `hash()` for initial hash generation

### Phase 5: Documentation and Polish
- Update package documentation
- Add docstrings to all new functions
- Verify backward compatibility
- Final testing and validation
