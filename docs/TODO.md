# Synth911gen2 - TODO List

## UPDATE 2025-06-20

1. Add the ability to select only specific call type(s) for more focused projects.
2. Translate call types into other languages.
3. Add the ability to adjust percentages for agency when using multiple agencies.
4. Add a GUID case number to each call.
5. Add Disposition Codes for each call. 
6. Add logic to the elapsed time fields to give P1 calls lower overall elapsed times more freqently.
7. Add the ability to use real address points as an option for calls, specifically to allow for the future enhancements listed below.

### Future Enhancements

I want to work on an injector process that could take generated calls and inject them into a live system. This would allow for testing of real-time systems with synthetic data. The injector could use a subset of the dataset to only supply things like the address, call type, and the priority then either write to a file that can be copied by a call-taker during testing, or if API access is available, inject the data directly into the system. This would allow for more realistic testing scenarios and could be a valuable tool for agencies looking to test their systems with synthetic data.

I believe that I can do this through serializing the data into a JSON object or a YAML file, I might even have to create a API that allows for data consumption then use a timeer to send the send data to the target at a specified interval. This would allow for a more realistic testing scenario and could be a valuable tool for agencies looking to test their systems with synthetic data.

