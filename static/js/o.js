function toggleStat(id) {
    var button = document.getElementById(id);
    var hiddenInput = document.getElementById(id + "_value");
    if (button.innerHTML === "Over") {
        button.innerHTML = "Under";
        hiddenInput.value = "Under";
    } else {
        button.innerHTML = "Over";
        hiddenInput.value = "Over";
    }
}