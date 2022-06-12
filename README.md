# GeoPyBangladesh

You can use it in **_Order Placement forms_** or in any other type of forms where **zilla and upazilla** input from **select (html tag)** is required.

* In `geodata.json` you have all the data required. Simple parse the JSON in your favourite language and use it anywhere.
* To fetch the latest geo data from http://www.bangladesh.gov.bd simple run `fetcher.py` and it will update `geodata.json`. But as zilla and upazilla names are almost static data, so you can safely use the repository's `geodata.json`. 

`geodata.json` file looks like this:

```{
    "চট্টগ্রাম বিভাগ": {
        "কুমিল্লা": [
            "নাঙ্গলকোট",
            "লাকসাম",
            .....
        ],
        "ফেনী": [
            "ছাগলনাইয়া উপজেলা",
            "ফুলগাজী উপজেলা",
            ....
        ],
        .... 
    },
    "রাজশাহী বিভাগ": {
        "সিরাজগঞ্জ": [
            "সিরাজগঞ্জ",
            "রায়গঞ্জ",
            ...],
        ...
    }
}

