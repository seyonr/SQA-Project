# To run:
# chmod +x scripts/run_tests.sh
# bash scripts/run_tests.sh

rm -rf scriptoutputs
mkdir scriptoutputs

# Loop through each subdirectory in "input/"
for subdir in input/*/; do
    # Get the base name of the subdirectory 
    folder_name=$(basename "$subdir")
    
    # Create corresponding subdirectory in "expectedoutputs"
    mkdir -p "scriptoutputs/$folder_name"
    
    # Process each test input file in the current subdirectory
    for infile in "$subdir"tc_*.in; do
        # Skip if no matching file is found
        [ -e "$infile" ] || continue
        
        # Get the base name without the .in extension (e.g., tc_login1)
        base_name=$(basename "$infile" .in)
        
        # Define the output filenames
        transaction_file="scriptoutputs/$folder_name/${base_name}.atf"
        terminal_output="scriptoutputs/$folder_name/${base_name}.oute"
        
        echo "Running test: $infile"
        
        # Run the script
        python3 phase3.py dummy_currentaccounts.txt "$transaction_file" < "$infile" > "$terminal_output"
    done
done
