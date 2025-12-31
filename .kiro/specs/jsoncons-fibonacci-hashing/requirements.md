# Requirements Document: jsoncons v1.0.5 - Fibonacci Hashing Integration

## Introduction

The `jsoncons` package is a Python CLI utility for handling JSON data and converting fixed-width COBOL data to JSON format. Version 1.0.5 extends the package with Fibonacci hashing capabilities, a multiplicative hashing technique that efficiently maps hash values to indices in power-of-2 sized hash tables. This version introduces new CLI commands and functions that demonstrate Fibonacci hashing principles while maintaining backward compatibility with existing functionality. Additionally, a Jupyter Notebook is included to demonstrate the performance characteristics and distribution benefits of Fibonacci hashing compared to traditional modulo and bitwise AND approaches.

## Glossary

- **Fibonacci Hashing**: A multiplicative hashing technique using a magic constant (approximately 2^64 / φ, where φ is the golden ratio) to map large hash values to smaller ranges, particularly effective for power-of-2 sized hash tables.
- **Magic Constant**: The value 11400714819323198485, derived from 2^64 / φ, used in Fibonacci hashing calculations.
- **Hash Table**: A data structure that uses a hash function to map keys to indices in an array.
- **Power-of-2 Table Size**: A hash table size that is a power of 2 (e.g., 8, 16, 32, 1024), enabling efficient bit-shift operations.
- **COBOL Data**: Fixed-width record format data commonly used in legacy business systems.
- **JSON**: JavaScript Object Notation, a lightweight data interchange format.
- **CLI Command**: A command-line interface operation that users invoke to perform specific tasks.
- **Property-Based Testing**: A testing methodology that verifies properties hold across a wide range of generated inputs.
- **Round-Trip Property**: A property that verifies data can be transformed and then reverse-transformed to produce equivalent results.

## Requirements

### Requirement 1: Fibonacci Hashing Function Implementation

**User Story:** As a developer, I want a Fibonacci hashing function available in the jsoncons package, so that I can efficiently map hash values to indices in power-of-2 sized hash tables.

#### Acceptance Criteria

1. WHEN the `fibonacci_hash_to_index` function is called with a valid 64-bit hash value and a power-of-2 table size THEN the system SHALL return an integer index within the valid range [0, table_size - 1]
2. WHEN the `fibonacci_hash_to_index` function is called with a table size that is not a power of 2 THEN the system SHALL raise a ValueError with a descriptive message
3. WHEN the `fibonacci_hash_to_index` function is called with a table size of 0 or negative THEN the system SHALL raise a ValueError
4. WHEN the `fibonacci_hash_to_index` function is called with different hash values THEN the system SHALL distribute the resulting indices across the available range without clustering
5. WHEN the `fibonacci_hash_to_index` function is called with the same hash value multiple times THEN the system SHALL return the same index consistently

### Requirement 2: Fibonacci Variant COBOL Parsing Function

**User Story:** As a developer, I want a Fibonacci variant of the COBOL parsing function, so that I can maintain consistent API patterns across the package.

#### Acceptance Criteria

1. WHEN `parse_cobol_line_fib` is called with valid COBOL data and a layout configuration THEN the system SHALL parse the data identically to the original `parse_cobol_line` function
2. WHEN `parse_cobol_line_fib` is called with invalid COBOL data THEN the system SHALL raise a CobolParsingError with descriptive context
3. WHEN `parse_cobol_line_fib` is called with data shorter than the expected record length THEN the system SHALL pad the data and log a warning
4. WHEN `parse_cobol_line_fib` processes numeric fields with implied decimals THEN the system SHALL correctly insert decimal points in the appropriate positions

### Requirement 3: Fibonacci Variant COBOL-to-JSON Processor

**User Story:** As a user, I want a Fibonacci variant of the COBOL-to-JSON conversion command, so that I can process COBOL data using the new variant functions.

#### Acceptance Criteria

1. WHEN the `cobol_to_json_fib` CLI command is invoked with a valid layout file and COBOL data file THEN the system SHALL convert the data to JSON and write it to the output file
2. WHEN the `cobol_to_json_fib` command processes multiple records THEN the system SHALL produce output identical to the original `cobol_to_json` command
3. WHEN the `cobol_to_json_fib` command encounters a parsing error on a specific line THEN the system SHALL log the error and skip that line, continuing with subsequent records
4. WHEN the `cobol_to_json_fib` command completes successfully THEN the system SHALL write valid JSON to the output file with proper formatting

### Requirement 4: Fibonacci Variant JSON Processing Command

**User Story:** As a user, I want a Fibonacci variant of the JSON processing command, so that I can maintain consistent command naming patterns.

#### Acceptance Criteria

1. WHEN the `process_json_fib` CLI command is invoked with valid JSON input THEN the system SHALL validate and format the JSON identically to the `encode` command
2. WHEN the `process_json_fib` command is called with the `--indent` option THEN the system SHALL apply the specified indentation level to the output
3. WHEN the `process_json_fib` command is called with the `--sort-keys` option THEN the system SHALL sort the keys in the output JSON
4. WHEN the `process_json_fib` command receives invalid JSON THEN the system SHALL report an error and exit with a non-zero status code

### Requirement 5: Fibonacci Hashing Demonstration Notebook

**User Story:** As a developer or researcher, I want a Jupyter Notebook that demonstrates Fibonacci hashing principles, so that I can understand its performance characteristics and distribution benefits.

#### Acceptance Criteria

1. WHEN the notebook is executed THEN the system SHALL generate sample COBOL data using the jsoncons tool
2. WHEN the notebook runs the performance benchmark THEN the system SHALL measure and display execution times for Fibonacci, modulo, and bitwise AND hashing methods
3. WHEN the notebook generates distribution analysis THEN the system SHALL create histograms showing how each hashing method distributes indices across the hash table
4. WHEN the notebook includes a visualization cell THEN the system SHALL demonstrate the Fibonacci hashing operation step-by-step with visual representation of the multiplication and bit-shift process
5. WHEN the notebook completes THEN the system SHALL clean up temporary files and provide clear conclusions about Fibonacci hashing benefits

### Requirement 6: Backward Compatibility and Error Handling

**User Story:** As a user, I want the new Fibonacci hashing features to coexist seamlessly with existing functionality, so that I can upgrade without breaking existing workflows.

#### Acceptance Criteria

1. WHEN existing CLI commands (`encode`, `decode`, `cobol_to_json`) are invoked THEN the system SHALL function identically to previous versions
2. WHEN the system encounters invalid input across all commands THEN the system SHALL provide clear, actionable error messages
3. WHEN the system processes data with encoding issues THEN the system SHALL handle them gracefully with appropriate logging
4. WHEN the system encounters file I/O errors THEN the system SHALL report them with sufficient context for troubleshooting

### Requirement 7: Comprehensive Test Coverage

**User Story:** As a developer, I want comprehensive tests for all new Fibonacci hashing functionality, so that I can ensure correctness and reliability.

#### Acceptance Criteria

1. WHEN unit tests are executed THEN the system SHALL verify that the `fibonacci_hash_to_index` function produces valid indices for various inputs
2. WHEN unit tests are executed THEN the system SHALL verify that `cobol_to_json_fib` produces identical output to `cobol_to_json`
3. WHEN unit tests are executed THEN the system SHALL verify that `process_json_fib` produces identical output to `encode`
4. WHEN property-based tests are executed THEN the system SHALL verify that Fibonacci hashing maintains consistency across all valid inputs
5. WHEN property-based tests are executed THEN the system SHALL verify that the hashing function distributes indices uniformly across the available range
