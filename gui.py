import streamlit as st
import json
import subprocess
import sys
from config import LOGITS_CONFIG, HIDDEN_CONFIG, DPO_CONFIG

# --- Helper Functions ---

def run_script(script_name, config):
    """
    Runs the selected distillation script with the given configuration.
    """
    try:
        # Save the updated config to a temporary file
        with open("temp_config.json", "w") as f:
            json.dump(config, f)

        # Construct the command to run the script
        command = [sys.executable, script_name, "--config", "temp_config.json"]

        # Start the subprocess and capture output
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True,
        )

        # Display live output
        st.write("--- Script Output ---")
        output_container = st.empty()
        output_text = ""
        for line in process.stdout:
            output_text += line
            output_container.code(output_text)

        process.wait()
        st.write("--- Script Finished ---")

        if process.returncode == 0:
            st.success(f"Successfully ran {script_name}")
        else:
            st.error(f"Error running {script_name}. See output above for details.")

    except Exception as e:
        st.error(f"An error occurred: {e}")


# --- GUI ---

st.title("DistillKit GUI")

# --- Script Selection ---
script_options = {
    "Logit-based Distillation": "distil_logits.py",
    "Hidden States-based Distillation": "distil_hidden.py",
    "DPO with Logit-based Distillation": "dpo_distil_logits.py",
}
selected_script_name = st.selectbox("Select a distillation script to run:", list(script_options.keys()))
selected_script_file = script_options[selected_script_name]

# --- Configuration Editor ---
st.header("Configuration")

# Get the corresponding config
if selected_script_file == "distil_logits.py":
    config = LOGITS_CONFIG
elif selected_script_file == "distil_hidden.py":
    config = HIDDEN_CONFIG
else:
    config = DPO_CONFIG

# Display the config editor
edited_config = st.text_area(
    "Edit Configuration (JSON format)",
    json.dumps(config, indent=4),
    height=400,
)

# --- Execution Control ---
if st.button("Run Script"):
    try:
        # Parse the edited config
        parsed_config = json.loads(edited_config)
        run_script(selected_script_file, parsed_config)
    except json.JSONDecodeError:
        st.error("Invalid JSON format in the configuration.")

# --- Config Export ---
st.sidebar.header("Export Configuration")
st.sidebar.download_button(
    label="Download Config as JSON",
    data=edited_config,
    file_name=f"{selected_script_file.replace('.py', '')}_config.json",
    mime="application/json",
)
