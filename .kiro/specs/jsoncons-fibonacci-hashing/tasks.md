# Implementation Plan: jsoncons v1.0.5 - Fibonacci Hashing Integration

- [x] 1. Implement Fibonacci Hashing Core Function





  - [x] 1.1 Add `fibonacci_hash_to_index()` function to `jsoncons/cli.py`


    - Implement 64-bit multiplication with wraparound using the magic constant
    - Calculate shift amount based on table size
    - Validate table size is a positive power of 2
    - Return index in valid range [0, table_size - 1]
    - _Requirements: 1.1, 1.2, 1.3_
  
  - [ ]* 1.2 Write property-based test for Fibonacci hash index range validity
    - **Property 1: Fibonacci Hash Index Range Validity**
    - **Validates: Requirements 1.1**
  
  - [ ]* 1.3 Write property-based test for Fibonacci hash consistency
    - **Property 2: Fibonacci Hash Consistency**
    - **Validates: Requirements 1.5**
  
  - [ ]* 1.4 Write property-based test for Fibonacci hash distribution uniformity
    - **Property 3: Fibonacci Hash Distribution Uniformity**
    - **Validates: Requirements 1.4**
  
  - [ ]* 1.5 Write unit tests for Fibonacci hash error handling
    - Test non-power-of-2 table sizes raise ValueError
    - Test zero and negative table sizes raise ValueError
    - Test error messages are descriptive
    - _Requirements: 1.2, 1.3_

- [ ] 2. Implement COBOL Parsing Variant Function
  - [ ] 2.1 Add `parse_cobol_line_fib()` function to `jsoncons/cli.py`
    - Implement as delegation to `parse_cobol_line()`
    - Maintain identical behavior and error handling
    - _Requirements: 2.1, 2.2, 2.3, 2.4_
  
  - [ ]* 2.2 Write property-based test for COBOL parsing equivalence
    - **Property 4: COBOL Parsing Equivalence**
    - **Validates: Requirements 2.1**
  
  - [ ]* 2.3 Write unit tests for COBOL parsing error handling
    - Test invalid numeric values raise CobolParsingError
    - Test error messages include line number and field context
    - Test short records are padded with warning logged
    - _Requirements: 2.2, 2.3_

- [ ] 3. Implement COBOL-to-JSON Processing Variant
  - [ ] 3.1 Add `process_cobol_to_json_fib()` function to `jsoncons/cli.py`
    - Load layout configuration from JSON file
    - Iterate through input lines using `parse_cobol_line_fib()`
    - Skip empty lines and handle parsing errors gracefully
    - Output valid JSON with DecimalEncoder for precision
    - Log informational and error messages to stderr
    - _Requirements: 3.1, 3.2, 3.3, 3.4_
  
  - [ ]* 3.2 Write property-based test for COBOL-to-JSON conversion equivalence
    - **Property 5: COBOL-to-JSON Conversion Equivalence**
    - **Validates: Requirements 3.2**
  
  - [ ]* 3.3 Write unit tests for COBOL-to-JSON error handling
    - Test missing layout file raises error
    - Test invalid layout JSON raises error
    - Test parsing errors are logged and processing continues
    - _Requirements: 3.3_

- [ ] 4. Implement JSON Processing Variant Function
  - [ ] 4.1 Add `process_json_fib()` function to `jsoncons/cli.py`
    - Implement as delegation to `process_json()`
    - Support indent and sort_keys options
    - Maintain identical behavior to original
    - _Requirements: 4.1, 4.2, 4.3, 4.4_
  
  - [ ]* 4.2 Write property-based test for JSON processing equivalence
    - **Property 6: JSON Processing Equivalence**
    - **Validates: Requirements 4.1**
  
  - [ ]* 4.3 Write unit tests for JSON processing options
    - Test various indent levels (0, 2, 4)
    - Test sort_keys option produces sorted output
    - Test invalid JSON raises JSONDecodeError
    - _Requirements: 4.2, 4.3, 4.4_

- [ ] 5. Add CLI Commands for Fibonacci Variants
  - [ ] 5.1 Add `process_json_fib` subcommand to argparse
    - Define arguments: infile, outfile, --indent, --sort-keys
    - Wire to `process_json_fib()` function
    - _Requirements: 4.1_
  
  - [ ] 5.2 Add `cobol_to_json_fib` subcommand to argparse
    - Define arguments: --layout-file, infile, outfile
    - Wire to `process_cobol_to_json_fib()` function
    - _Requirements: 3.1_
  
  - [ ]* 5.3 Write CLI integration tests for new commands
    - Test `process_json_fib` with stdin/stdout
    - Test `process_json_fib` with file I/O
    - Test `cobol_to_json_fib` with valid data
    - Test error handling and exit codes
    - _Requirements: 3.1, 4.1_

- [ ] 6. Checkpoint - Ensure all core functionality tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 7. Implement Demonstration Jupyter Notebook
  - [ ] 7.1 Create `Fibonacci_Hashing_Demo.ipynb` notebook structure
    - Add markdown cells explaining Fibonacci hashing concepts
    - Add code cells for imports and setup
    - _Requirements: 5.1_
  
  - [ ] 7.2 Implement data generation cell
    - Generate sample COBOL data using jsoncons tool
    - Load generated JSON data for hashing demonstration
    - _Requirements: 5.1_
  
  - [ ] 7.3 Implement performance benchmark cell
    - Define hashing functions (Fibonacci, modulo, bitwise AND)
    - Measure execution times for each method
    - Display timing results
    - _Requirements: 5.2_
  
  - [ ] 7.4 Implement distribution analysis visualization
    - Calculate indices using each hashing method
    - Create histograms showing distribution across hash table
    - Display side-by-side comparison
    - _Requirements: 5.3_
  
  - [ ] 7.5 Implement Fibonacci hashing operation visualization cell
    - Create step-by-step visual demonstration of:
      - Input hash value
      - Multiplication by magic constant
      - Bit-shift operation
      - Final index result
    - Show example with specific values
    - _Requirements: 5.4_
  
  - [ ] 7.6 Implement cleanup and conclusions cell
    - Remove temporary files created during execution
    - Provide clear conclusions about Fibonacci hashing benefits
    - Summarize performance and distribution findings
    - _Requirements: 5.5_

- [ ] 8. Verify Backward Compatibility
  - [ ] 8.1 Test existing CLI commands unchanged
    - Run `encode` command and verify output identical to v1.0.4
    - Run `decode` command and verify output identical to v1.0.4
    - Run `cobol_to_json` command and verify output identical to v1.0.4
    - _Requirements: 6.1_
  
  - [ ]* 8.2 Write property-based test for backward compatibility
    - **Property 10: Backward Compatibility**
    - **Validates: Requirements 6.1**

- [ ] 9. Implement Comprehensive Error Handling Tests
  - [ ]* 9.1 Write property-based test for error handling consistency
    - **Property 7: Fibonacci Hash Error Handling**
    - **Validates: Requirements 1.2, 1.3**
  
  - [ ]* 9.2 Write property-based test for COBOL parsing error handling
    - **Property 8: COBOL Parsing Error Handling**
    - **Validates: Requirements 2.2**
  
  - [ ]* 9.3 Write property-based test for JSON validation round-trip
    - **Property 9: JSON Validation Round-Trip**
    - **Validates: Requirements 4.4**
  
  - [ ]* 9.4 Write unit tests for error message quality
    - Test all error messages are clear and actionable
    - Test error messages include sufficient context
    - _Requirements: 6.2, 6.3, 6.4_

- [ ] 10. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 11. Documentation and Final Polish
  - [ ] 11.1 Add docstrings to all new functions
    - Document `fibonacci_hash_to_index()` with parameters, returns, raises
    - Document `parse_cobol_line_fib()` with behavior notes
    - Document `process_cobol_to_json_fib()` with behavior notes
    - Document `process_json_fib()` with behavior notes
    - _Requirements: 1.1, 2.1, 3.1, 4.1_
  
  - [ ] 11.2 Update package README
    - Add section describing Fibonacci hashing feature
    - Document new CLI commands with examples
    - Reference the demonstration notebook
    - _Requirements: 5.1_
  
  - [ ] 11.3 Update CHANGELOG
    - Document v1.0.5 release notes
    - List new features and improvements
    - Note backward compatibility
    - _Requirements: 6.1_
  
  - [ ] 11.4 Verify code quality
    - Run linter (pylint/flake8) on all new code
    - Ensure code follows project style guidelines
    - Check for any warnings or issues
    - _Requirements: 1.1, 2.1, 3.1, 4.1_

- [ ] 12. Final Checkpoint - Ensure all tests pass and documentation is complete
  - Ensure all tests pass, ask the user if questions arise.
