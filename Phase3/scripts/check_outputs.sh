# To run:
# chmod +x scripts/check_outputs.sh
# bash scripts/check_outputs.sh

pass_count=0
fail_count=0

# Find all files in expectedoutputs and loop over them.
while IFS= read -r -d '' expected_file; do
    # Remove the expectedoutputs/ prefix to get the relative path.
    rel_path="${expected_file#expectedoutputs/}"
    script_file="scriptoutputs/${rel_path%.out}.oute"

    # Check if the corresponding file exists in scriptoutputs.
    if [ ! -f "$script_file" ]; then
        echo "FAIL: $rel_path (missing in scriptoutputs)"
        fail_count=$((fail_count+1))
    else
        # Use diff to compare the two files.
        if diff -q "$expected_file" "$script_file" > /dev/null; then
            echo "PASS: $rel_path"
            pass_count=$((pass_count+1))
        else
            echo "FAIL: $rel_path"
            echo "Differences:"
            diff "$expected_file" "$script_file"
            fail_count=$((fail_count+1))
        fi
    fi
done < <(find expectedoutputs -type f -print0)

echo "Summary: $pass_count passed, $fail_count failed."
