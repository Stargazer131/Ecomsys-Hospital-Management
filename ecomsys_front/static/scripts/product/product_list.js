function startVoiceRecognition() {
  const recognition = new webkitSpeechRecognition();
  const voiceSearchButton = document.getElementById("recordingButton");

  // Change the button color to red when recognition starts
  const originalColor = voiceSearchButton.style.backgroundColor;

  recognition.onstart = function () {
    voiceSearchButton.style.backgroundColor = "red";
  };

  recognition.onresult = function (event) {
    const result = event.results[0][0].transcript;
    document.getElementById("voiceSearch").value = result;
  };

  recognition.onend = function () {
    // Change the button color back to the original color when recognition ends
    voiceSearchButton.style.backgroundColor = originalColor;
  };

  recognition.start();
}

document.addEventListener("DOMContentLoaded", function () {
  // Get references to the search type select and the search options
  var searchTypeSelect = document.getElementById("searchType");
  var productTypeSelect = document.getElementById("productType");

  var bookFieldsLabel = document.querySelector('label[for="bookFields"]');
  var bookFieldsSelect = document.getElementById("bookFields");

  var clothesFieldsLabel = document.querySelector('label[for="clothesFields"]');
  var clothesFieldsSelect = document.getElementById("clothesFields");

  var mobileFieldsLabel = document.querySelector('label[for="mobileFields"]');
  var mobileFieldsSelect = document.getElementById("mobileFields");

  var textSearchLabel = document.querySelector('label[for="textSearch"]');
  var textSearchInput = document.getElementById("textSearch");

  var imageSearchLabel = document.querySelector('label[for="imageSearch"]');
  var imageSearchInput = document.getElementById("imageSearch");
  var previewImage = document.getElementById("imagePreview");

  var voiceSearchLabel = document.querySelector('label[for="voiceSearch"]');
  var voiceSearchInput = document.getElementById("voiceSearch");
  var voiceRecordingButton = document.getElementById("recordingButton");

  // Function to show or hide search options based on the selected search type
  function toggleSearchOptions() {
    var selectedSearchType = searchTypeSelect.value;

    // Hide all search options and labels initially
    textSearchLabel.style.display = "none";
    textSearchInput.style.display = "none";

    imageSearchLabel.style.display = "none";
    imageSearchInput.style.display = "none";
    previewImage.style.display = "none";

    voiceSearchLabel.style.display = "none";
    voiceSearchInput.style.display = "none";
    voiceRecordingButton.style.display = "none";

    // Show the selected search option and label
    if (selectedSearchType === "text") {
      textSearchLabel.style.display = "block";
      textSearchInput.style.display = "block";
    } else if (selectedSearchType === "image") {
      imageSearchLabel.style.display = "block";
      imageSearchInput.style.display = "block";
      previewImage.style.display = "block";

      bookFieldsLabel.style.display = "none";
      bookFieldsSelect.style.display = "none";
      clothesFieldsLabel.style.display = "none";
      clothesFieldsSelect.style.display = "none";
      mobileFieldsLabel.style.display = "none";
      mobileFieldsSelect.style.display = "none";

    } else if (selectedSearchType === "voice") {
      voiceSearchLabel.style.display = "block";
      voiceSearchInput.style.display = "block";
      voiceRecordingButton.style.display = "block";
    }
  }

  function toggleProductTypeOptions() {
    var selectedProductType = productTypeSelect.value;
    var selectedSearchType = searchTypeSelect.value;

    bookFieldsLabel.style.display = "none";
    bookFieldsSelect.style.display = "none";

    clothesFieldsLabel.style.display = "none";
    clothesFieldsSelect.style.display = "none";

    mobileFieldsLabel.style.display = "none";
    mobileFieldsSelect.style.display = "none";

    if (selectedSearchType == "image") {
      return;
    }

    if (selectedProductType == "book") {
      bookFieldsLabel.style.display = "block";
      bookFieldsSelect.style.display = "block";
    } else if (selectedProductType == "clothes") {
      clothesFieldsLabel.style.display = "block";
      clothesFieldsSelect.style.display = "block";
    } else if (selectedProductType == "mobile") {
      mobileFieldsLabel.style.display = "block";
      mobileFieldsSelect.style.display = "block";
    }
  }

  // Attach the toggleSearchOptions function to the change event of the search type select
  searchTypeSelect.addEventListener("change", toggleSearchOptions);
  // searchTypeSelect.addEventListener("change", toggleProductTypeOptions);

  // productTypeSelect.addEventListener("change", toggleSearchOptions);
  productTypeSelect.addEventListener("change", toggleProductTypeOptions);

  // Call the function initially to set the initial state based on the default selected value
  toggleSearchOptions();
  toggleProductTypeOptions();
});

function previewImage(input) {
  var preview = document.getElementById("imagePreview");
  var container = document.getElementById("imagePreviewContainer");

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      preview.src = e.target.result;
      preview.style.display = "block";
      container.style.display = "block";
    };

    reader.readAsDataURL(input.files[0]);
  }
}
