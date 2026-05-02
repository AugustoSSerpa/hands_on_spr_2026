<button onclick="copyToClipboard('The prompt text that you want to copy here!');">Copy Prompt</button>

<script>
function copyToClipboard(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);
}
</script>