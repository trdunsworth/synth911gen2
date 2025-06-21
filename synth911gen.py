#!/usr/bin/env python

import fireducks.pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from faker import Faker
from faker.providers import DynamicProvider
import argparse
import re
import sys
from shared.constants import DEFAULT_LOCALE, validate_locale

# Try to import PyInquirer, but provide fallback if it's not available
try:
    from PyInquirer import prompt, Validator, ValidationError
    PYINQUIRER_AVAILABLE = True
except ImportError:
    print("Warning: PyInquirer is not available. Using command-line arguments instead.")
    PYINQUIRER_AVAILABLE = False

    # Define a simple validator class for compatibility
    class Validator:
        def validate(self, document):
            pass

    class ValidationError(Exception):
        def __init__(self, message, cursor_position):
            self.message = message
            self.cursor_position = cursor_position
            super().__init__(message)

def sanitize_input(user_input):
    # Regular expression to match allowed characters
    pattern = r'^[a-zA-Z0-9\s\-]+$'
    if not re.match(pattern, user_input):
        raise ValueError("Input contains invalid characters. Only letters, numbers, spaces, and hyphens are allowed.")
    return user_input

def sanitize_cli():
    """
    A utility function to test input sanitization from the command line.
    This is separate from the main data generation functionality.
    """
    parser = argparse.ArgumentParser(description="Sanitize user input options in synth911gen.py")

    # Example of a command-line argument
    parser.add_argument('--option', type=str, required=True, help='User input option')

    args = parser.parse_args()

    try:
        sanitized_option = sanitize_input(args.option)
        print(f"Sanitized Option: {sanitized_option}")
    except ValueError as e:
        print(e)

# Note: This function is for testing sanitization only
# The actual entry point is at the bottom of the file

fake = None  # Will be initialized in generate_911_data with the specified locale

# Law enforcement problems with their associated priority levels
# Priority 1: Immediate response, life-threatening
# Priority 2: Urgent response, potential for harm
# Priority 3: Prompt response, no immediate danger
# Priority 4: Routine response, minor issues
# Priority 5: Non-urgent, administrative or delayed response

LAW_PROBLEMS = [
    # Priority 1 (Immediate response, life-threatening)
    ("WEAPON VIOL GUN IN PROG", 1),
    ("ALARM RESIDENTIAL NIGHTIME", 1),
    ("ROBBERY IN PROGRESS", 1),
    ("SHOOTING", 1),
    ("STABBING", 1),
    ("OFFICER NEEDS ASSISTANCE", 1),
    ("HOSTAGE SITUATION", 1),
    ("SUICIDAL SUBJECT", 1),

    # Priority 2 (Urgent response, potential for harm)
    ("DOMESTIC VIOL NO INJ", 2),
    ("DOMESTIC VIOL WITH INJ", 2),
    ("DWI - DRUNK/INTOX DRIVER", 2),
    ("DISORDERLY CONDUCT", 2),
    ("911 HANG UP", 2),
    ("ASSAULT", 2),
    ("BURGLARY IN PROGRESS", 2),
    ("SUSPICIOUS PERSON WITH WEAPON", 2),

    # Priority 3 (Prompt response, no immediate danger)
    ("SUSPICIOUS EVENT", 3),
    ("SUSPICIOUS PERSON", 3),
    ("SUSPICIOUS VEHICLE", 3),
    ("TRESPASSING", 3),
    ("LARCENY IN PROGRESS", 3),
    ("TRAFFIC ACCIDENT NO INJURY", 3),
    ("ALARM COMMERCIAL", 3),

    # Priority 4 (Routine response, minor issues)
    ("NOISE COMPLAINT IN PROG", 4),
    ("NOISE COMPLAINT DELAY", 4),
    ("PARKING COMPLAINT", 4),
    ("TRAFFIC STOP", 4),
    ("DISABLED MOTORIST", 4),
    ("PUBLIC SERVICE - LAW", 4),
    ("ASSIST CITIZEN", 4),

    # Priority 5 (Non-urgent, administrative or delayed)
    ("PROPERTY LOST TRU", 5),
    ("POLICE INFORMATION", 5),
    ("FOLLOW UP", 5),
    ("LARCENY REPORT", 5),
    ("FRAUD REPORT", 5),
    ("VANDALISM REPORT", 5),
    ("MENTAL HEALTH", 5),
    ("DRUG COMPLAINT", 5),
    ("FLAG DOWN", 5),
    ("GLA", 5),
]

# Create the DynamicProvider with just the problem names
law_problem_provider = DynamicProvider(
    provider_name="law_problem",
    elements=[problem for problem, _ in LAW_PROBLEMS]
)

# Fire problems with their associated priority levels
# Priority 1: Immediate response, life-threatening
# Priority 2: Urgent response, potential for harm
# Priority 3: Prompt response, no immediate danger
# Priority 4: Routine response, minor issues
# Priority 5: Non-urgent, administrative or delayed response

FIRE_PROBLEMS = [
    # Priority 1 (Immediate response, life-threatening)
    ("RESIDENTIAL BUILDING FIRE", 1),
    ("HIGHRISE BUILDING FIRE", 1),
    ("COMMERCIAL BUILDING FIRE", 1),
    ("ENTRAPMENT", 1),
    ("MVC SCHOOL BUS", 1),
    ("HAZMAT MAJOR", 1),
    ("STRUCTURE COLLAPSE", 1),

    # Priority 2 (Urgent response, potential for harm)
    ("MVC AUTO", 2),
    ("GAS LEAK", 2),
    ("CO ALARM", 2),
    ("OUTSIDE FIRE", 2),
    ("APPLIANCE FIRE", 2),
    ("MVC MOTORCYCLE", 2),
    ("WIRES DOWN", 2),
    ("HAZMAT", 2),

    # Priority 3 (Prompt response, no immediate danger)
    ("FIRE ALARM", 3),
    ("ELEVATOR", 3),
    ("ODOR OF SMOKE", 3),
    ("WATER LEAK", 3),
    ("SMOKE DETECTOR", 3),

    # Priority 4 (Routine response, minor issues)
    ("PUBLIC SERVICE - FIRE", 4),
    ("LOCKOUT", 4),
    ("ASSIST CITIZEN - FIRE", 4),
    ("ANIMAL RESCUE", 4),

    # Priority 5 (Non-urgent, administrative or delayed)
    ("FIRE INSPECTION", 5),
    ("FIRE PREVENTION", 5),
    ("FIRE EDUCATION", 5),
    ("SMOKE DETECTOR INSTALLATION", 5),
]

# Create the DynamicProvider with just the problem names
fire_problem_provider = DynamicProvider(
    provider_name="fire_problem",
    elements=[problem for problem, _ in FIRE_PROBLEMS]
)

# EMS problems with their associated priority levels
# Priority 1: Immediate response, life-threatening
# Priority 2: Urgent response, potential for harm
# Priority 3: Prompt response, no immediate danger
# Priority 4: Routine response, minor issues
# Priority 5: Non-urgent, administrative or delayed response

EMS_PROBLEMS = [
    # Priority 1 (Immediate response, life-threatening)
    ("CARDIAC ARREST ALS", 1),
    ("UNCONSCIOUS ALS", 1),
    ("ALTERED LOC ALS", 1),
    ("STROKE ALS", 1),
    ("MUTUAL ALS", 1),
    ("ALLERGIC REACTION ALS", 1),
    ("OVERDOSE ALS", 1),
    ("TRAUMATIC INJURY ALS", 1),
    ("DROWNING", 1),

    # Priority 2 (Urgent response, potential for harm)
    ("TROUBLE BREATHING ALS", 2),
    ("CHEST PAIN ALS", 2),
    ("HEART PROBLEMS ALS", 2),
    ("SEIZURE ALS", 2),
    ("DIABETIC EMERGENCY ALS", 2),
    ("ASSAULT ALS", 2),
    ("PSYCHIATRIC EMERGENCY ALS", 2),
    ("ALS EMERGENCY", 2),

    # Priority 3 (Prompt response, no immediate danger)
    ("BLS EMERGENCY", 3),
    ("FALL BLS", 3),
    ("INJURED PERSON BLS", 3),
    ("BACK PAIN BLS", 3),
    ("HEADACHE BLS", 3),
    ("SICK PERSON BLS", 3),

    # Priority 4 (Routine response, minor issues)
    ("PUBLIC SERICE EMS", 4),
    ("MINOR MEDICAL", 4),
    ("ASSIST CITIZEN - EMS", 4),

    # Priority 5 (Non-urgent, administrative or delayed)
    ("MEDICAL ALARM", 5),
    ("ROUTINE TRANSPORT", 5),
    ("MENTAL HEALTH ALS", 5),
    ("WELFARE CHECK", 5),
]

# Create the DynamicProvider with just the problem names
ems_problem_provider = DynamicProvider(
    provider_name="ems_problem",
    elements=[problem for problem, _ in EMS_PROBLEMS]
)

# RESCUE problems with their associated priority levels
# Priority 1: Immediate response, life-threatening
# Priority 2: Urgent response, potential for harm
# Priority 3: Prompt response, no immediate danger
# Priority 4: Routine response, minor issues
# Priority 5: Non-urgent, administrative or delayed response

RESCUE_PROBLEMS = [
    # Priority 1 (Immediate response, life-threatening)
    ("WATER RESCUE IN PROGRESS", 1),
    ("MOUNTAIN RESCUE IN PROGRESS", 1),
    ("VEHICLE EXTRICATION WITH ENTRAPMENT", 1),
    ("CONFINED SPACE RESCUE", 1),
    ("HIGH ANGLE RESCUE", 1),
    ("SEARCH AND RESCUE - MISSING PERSON", 1),
    ("TECHNICAL RESCUE - STRUCTURE COLLAPSE", 1),

    # Priority 2 (Urgent response, potential for harm)
    ("WATER RESCUE STANDBY", 2),
    ("MOUNTAIN RESCUE STANDBY", 2),
    ("VEHICLE EXTRICATION NO ENTRAPMENT", 2),
    ("SEARCH AND RESCUE - NON-CRITICAL", 2),
    ("ANIMAL RESCUE - DANGEROUS SITUATION", 2),

    # Priority 3 (Prompt response, no immediate danger)
    ("ANIMAL RESCUE - NON-URGENT", 3),
    ("PUBLIC ASSIST RESCUE", 3),
    ("STANDBY FOR EVENT", 3),

    # Priority 4 (Routine response, minor issues)
    ("EQUIPMENT CHECK RESCUE", 4),
    ("TRAINING EXERCISE RESCUE", 4),
    ("PUBLIC EDUCATION RESCUE", 4),

    # Priority 5 (Non-urgent, administrative or delayed)
    ("RESCUE REPORT ONLY", 5),
    ("RESCUE INFORMATION", 5),
    ("FOLLOW UP RESCUE", 5),
]

# Create the DynamicProvider with just the problem names
rescue_problem_provider = DynamicProvider(
    provider_name="rescue_problem",
    elements=[problem for problem, _ in RESCUE_PROBLEMS]
)

# List of Dispositions
# These are the final outcomes of a call, which can be used to indicate how the call was resolved.
DISPOSITIONS = [
    "CANCELLED",
    "NO ACTION TAKEN",
    "REFERRED TO OTHER AGENCY",
    "REPORT TAKEN",
    "ARREST MADE",
    "CITATION ISSUED",
    "UNIT CLEARED",
    "TAKEN TO HOSPITAL",
]

# Create a DynamicProvider for dispositions
disposition_provider = DynamicProvider(
    provider_name="disposition",
    elements=DISPOSITIONS
)

# Street address provider will be created in the generate_911_data function
# after Faker is initialized with the specified locale

# TODO: Hook this to a web interface to allow users to generate data on demand.

def filter_agencies(agencies, selected_agencies):
    """
    Filter the list of agencies based on user selection.

    Args:
        agencies (list): List of all available agencies
        selected_agencies (list): List of agencies selected by the user

    Returns:
        list: Filtered list of agencies
    """
    if not selected_agencies:
        # If no selection made, return all agencies
        return agencies

    # Validate selected agencies and filter out invalid ones
    invalid_agencies = [agency for agency in selected_agencies if agency not in agencies]
    if invalid_agencies:
        print(f"Warning: The following selected agencies are not valid and will be ignored: {', '.join(invalid_agencies)}")

    # Return only the valid selected agencies
    return [agency for agency in agencies if agency in selected_agencies]

def generate_911_data(num_records=10000, start_date=None, end_date=None, num_names=8, locale=DEFAULT_LOCALE, selected_agencies=None, agency_probabilities=None):
    """
    This function generates synthetic 911 dispatch data for a given number of records. This will output a CSV file with the generated data.
    The data includes various fields such as call_id, agency, event_time, day_of_year, week_no, hour, day_night, dow, shift, shift_part, problem, address, priority_number, call_taker, call_reception, dispatcher, queue_time, dispatch_time, phone_time, ack_time, enroute_time, on_scene_time, process_time, total_time and time stamps for various events.

    Args:
        num_records (int, optional): Number of records to generate. Defaults to 10000.
        start_date (str, optional): Start date in YYYY-MM-DD format. Defaults to "2024-01-01".
        end_date (str, optional): End date in YYYY-MM-DD format. Defaults to "2024-12-31".
        num_names (int, optional): Number of names to generate per shift. Defaults to 8.
        locale (str, optional): Faker locale for generating localized data. Defaults to "en_US".
                               Examples: "en_GB" (British English), "fr_FR" (French), "de_DE" (German), etc.
        selected_agencies (list, optional): List of agencies to include. Defaults to None (all agencies).
        agency_probabilities (list, optional): List of probabilities for each agency. Defaults to None.

        This needs to be run with the following setup: python synth911gen.py -n 10000 -s 2024-01-01 -e 2024-12-31 -o computer_aided_dispatch.csv
    """
    # Validate locale before proceeding
    if not validate_locale(locale):
        print(f"Warning: Unsupported locale '{locale}'. Falling back to {DEFAULT_LOCALE}")
        locale = DEFAULT_LOCALE

    # Initialize Faker with the specified locale
    global fake
    fake = Faker(locale)

    # Generate address list with the specified locale
    address_list = [fake.unique.street_address() for _ in range(2500)]

    # Create street address provider
    street_address_provider = DynamicProvider(
        provider_name="street_address", elements=address_list
    )

    def generate_names(num_names=8):
        """
        This function generates a list of random names using the Faker library. The number of names generated is determined by the num_names parameter.
        The names are generated in the format "Last, First". This function is used to create call_taker and dispatcher names for the generated data and conforms to the most commonly used formats.

        Args:
            num_names (int, optional): _description_. Defaults to 8.

        Returns:
            dictionary: This returns a dictionary with keys A, B, C, D and values as lists of names.
        """
        return [f"{fake.last_name()}, {fake.first_name()}" for _ in range(num_names)]

    call_taker_names = {key: generate_names(num_names) for key in ["A", "B", "C", "D"]}
    dispatcher_names = {key: generate_names(num_names) for key in ["A", "B", "C", "D"]}

    # Define the probabilities for each agency
    probabilities = [0.72, 0.15, 0.10, 0.03]  # LAW, EMS, FIRE, RESCUE
    agencies = ["LAW", "EMS", "FIRE", "RESCUE"]

    # Filter agencies based on user selection
    filtered_agencies = filter_agencies(agencies, selected_agencies)

    # Handle user-specified probabilities
    if agency_probabilities is not None:
        if len(agency_probabilities) != len(filtered_agencies):
            raise ValueError("Number of agency probabilities must match number of selected agencies.")
        if not np.isclose(sum(agency_probabilities), 1.0):
            raise ValueError("Agency probabilities must sum to 1.")
        probabilities = agency_probabilities
    elif len(filtered_agencies) < len(agencies):
        probabilities = [1.0 / len(filtered_agencies)] * len(filtered_agencies)
    else:
        probabilities = [0.72, 0.15, 0.10, 0.03]

    # Generate the agency column with the specified distribution
    agency_choices = np.random.choice(filtered_agencies, size=num_records, p=probabilities)

    # Map agency to prefix
    agency_prefix = {"LAW": "L", "EMS": "M", "FIRE": "F", "RESCUE": "R"}

    # Set default start and end dates if not provided
    if start_date is None:
        start_date = "2024-01-01"
    if end_date is None:
        end_date = "2024-12-31"

    # Convert start_date and end_date to datetime objects
    start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")

    # Get the year from start date for call_id prefix
    year_suffix = str(start_date_dt.year)[-2:]

    # Determine starting numbers for each agency
    def get_start_number():
        if start_date_dt.month == 1 and start_date_dt.day == 1:
            return 1
        else:
            # Generate a random starting number between 1000 and 100000
            return random.randint(1000, 100000)

    # Generate sequential numbers for each agency
    agency_counters = {
        "L": get_start_number(),
        "M": get_start_number(),
        "F": get_start_number(),
        "R": get_start_number()
    }
    call_ids_full = []

    for agency in agency_choices:
        prefix = agency_prefix[agency]
        call_id = f"{year_suffix}-{prefix}{agency_counters[prefix]:06d}"
        call_ids_full.append(call_id)
        agency_counters[prefix] += 1

    # Generate random datetimes within the specified range
    date_range = int((end_date_dt - start_date_dt).total_seconds())
    random_seconds = np.random.randint(0, date_range, size=num_records)
    datetimes_full = [
        start_date_dt + timedelta(seconds=int(sec)) for sec in sorted(random_seconds)
    ]

    # Create DataFrame
    df_full = pd.DataFrame(
        {
            "call_id": call_ids_full,
            "agency": agency_choices,
            "event_time": datetimes_full,
        }
    )

    # Sort the DataFrame by event_time to ensure chronological order
    df_full = df_full.sort_values("event_time").reset_index(drop=True)

    # Add day_of_year column
    df_full["day_of_year"] = df_full["event_time"].dt.dayofyear

    # Add week_no column
    df_full["week_no"] = df_full["event_time"].dt.isocalendar().week

    # Add hour column
    df_full["hour"] = df_full["event_time"].dt.hour

    # Add day_night column based on the hour column
    df_full["day_night"] = df_full["hour"].apply(
        lambda x: "DAY" if 6 <= x <= 17 else "NIGHT"
    )

    # Add dow column with the day of the week in 3-character format
    df_full["dow"] = df_full["event_time"].dt.strftime("%a").str.upper()

    # Define the function to determine the shift
    def determine_shift(row):
        """
        This is a function to determine the shift based on the week number, day_night, and day of the week (dow).
        The function uses the following logic:
        - If the week number is even:
            - DAY on MON, TUE, FRI, SAT -> A
            - NIGHT on MON, TUE, FRI, SAT -> C
            - DAY on WED, THU, SUN -> B
            - NIGHT on WED, THU, SUN -> D
        - This mirrors an existing shift pattern employed by agencies that use a 12 hour shift schedule.

        Args:
            row (_type_): _description_

        Returns:
            string: This returns the shift based on the logic defined above.
        """
        if row["week_no"] % 2 == 0:
            if row["day_night"] == "DAY" and row["dow"] in ["MON", "TUE", "FRI", "SAT"]:
                return "A"
            elif row["day_night"] == "NIGHT" and row["dow"] in [
                "MON",
                "TUE",
                "FRI",
                "SAT",
            ]:
                return "C"
            elif row["day_night"] == "DAY" and row["dow"] in ["WED", "THU", "SUN"]:
                return "B"
            elif row["day_night"] == "NIGHT" and row["dow"] in ["WED", "THU", "SUN"]:
                return "D"
        else:
            if row["day_night"] == "DAY" and row["dow"] in ["WED", "THU", "SUN"]:
                return "A"
            elif row["day_night"] == "NIGHT" and row["dow"] in ["WED", "THU", "SUN"]:
                return "C"
            elif row["day_night"] == "DAY" and row["dow"] in [
                "MON",
                "TUE",
                "FRI",
                "SAT",
            ]:
                return "B"
            elif row["day_night"] == "NIGHT" and row["dow"] in [
                "MON",
                "TUE",
                "FRI",
                "SAT",
            ]:
                return "D"

    # Apply the function to create the shift column
    df_full["shift"] = df_full.apply(determine_shift, axis=1)

    # Define the function to determine the shift_part
    def determine_shift_part(hour):
        """
        This determines how the shift is divided into parts based on the hour of the day. This breaks a 12-hour shift into 3 parts:

        Args:
            hour (int): This is the hour compoenent of the event_time datetime column.

        Returns:
            string: A descriptor of the shift part based on the hour.
        """
        if hour in [6, 7, 8, 9, 18, 19, 20, 21]:
            return "EARLY"
        elif hour in [10, 11, 12, 13, 22, 23, 0, 1]:
            return "MIDS"
        else:
            return "LATE"

    # Apply the function to create the shift_part column
    df_full["shift_part"] = df_full["hour"].apply(determine_shift_part)

    # Assign problem type based on agency
    def assign_problem(agency):
        """
        This function assigns a problem type based on the agency type. It uses the Faker library to generate random problems for each agency.

        Args:
            agency (string): This is the agency type (LAW, EMS, FIRE).

        Returns:
            string: A random problem type based on the agency.
        """
        if agency == "LAW":
            return fake.law_problem()
        elif agency == "FIRE":
            return fake.fire_problem()
        elif agency == "EMS":
            return fake.ems_problem()
        elif agency == "RESCUE":
            return fake.rescue_problem()
        else:
            return None

    # Register the dynamic providers with Faker
    fake.add_provider(law_problem_provider)
    fake.add_provider(fire_problem_provider)
    fake.add_provider(ems_problem_provider)
    fake.add_provider(disposition_provider)
    fake.add_provider(rescue_problem_provider)

    df_full["problem"] = df_full["agency"].apply(assign_problem)

    # Add address column with a street address

    fake.add_provider(street_address_provider)

    df_full["address"] = [fake.street_address() for _ in range(len(df_full))]

    # Create dictionaries to map problems to their priority numbers
    law_priority_map = {problem: priority for problem, priority in LAW_PROBLEMS}
    fire_priority_map = {problem: priority for problem, priority in FIRE_PROBLEMS}
    ems_priority_map = {problem: priority for problem, priority in EMS_PROBLEMS}
    rescue_priority_map = {problem: priority for problem, priority in RESCUE_PROBLEMS}

    # Function to assign priority number based on agency and problem
    def assign_priority(row):
        agency = row["agency"]
        problem = row["problem"]

        if agency == "LAW":
            # Use the law priority map, default to 3 if problem not found
            return law_priority_map.get(problem, 3)
        elif agency == "FIRE":
            # Use the fire priority map, default to 3 if problem not found
            return fire_priority_map.get(problem, 3)
        elif agency == "EMS":
            # Use the ems priority map, default to 3 if problem not found
            return ems_priority_map.get(problem, 3)
        elif agency == "RESCUE":
            # Use the rescue priority map, default to 3 if problem not found
            return rescue_priority_map.get(problem, 3)
        else:
            # Default priority for unknown agency
            return 3

    # Add priority_number column based on the problem type and agency
    df_full["priority_number"] = df_full.apply(assign_priority, axis=1)

    # Define a function to assign call_taker based on shift
    def assign_call_taker(shift):
        """
        This function assigns a call_taker based on the shift. It uses the Faker library to generate random names for each shift.

        Args:
            shift (string): This is the shift type (A, B, C, D).

        Returns:
            string: The name of the call_taker based on the shift.
        """
        return random.choice(call_taker_names[shift])

    # Apply the function to create the call_taker column
    df_full["call_taker"] = df_full["shift"].apply(assign_call_taker)

    # Define the probabilities for each call reception method
    probabilities_reception = [0.55, 0.20, 0.10, 0.10, 0.05]

    # Define the call reception categories
    reception_methods = ["E-911", "PHONE", "OFFICER", "TEXT", "C2C"]

    # Generate the call_reception column with the specified distribution
    df_full["call_reception"] = np.random.choice(
        reception_methods, size=len(df_full), p=probabilities_reception
    )

    # Define a function to assign dispatcher based on shift
    def assign_dispatcher(shift):
        """
        This function assigns a dispatcher based on the shift. It uses the Faker library to generate random names for each shift.

        Args:
            shift (string): This is the shift type (A, B, C, D).

        Returns:
            string: The name of the dispatcher based on the shift.
        """
        return random.choice(dispatcher_names[shift])

    # Apply the function to create the dispatcher column
    df_full["dispatcher"] = df_full["shift"].apply(assign_dispatcher)

    mu = 3.5
    sigma = 1.2

    # Generate columns with distributions
    df_full["queue_time"] = np.random.lognormal(
        mean=mu, sigma=sigma, size=len(df_full)
    ).astype(int)
    df_full["queue_time"] = (
        df_full["queue_time"] * 200 / df_full["queue_time"].mean()
    ).astype(int)
    df_full["queue_time"] = df_full["queue_time"].clip(lower=0, upper=90)

    shape, scale = 3.0, 45.0
    df_full["dispatch_time"] = (
        np.random.chisquare(df=5, size=len(df_full)) * 2
    ).astype(int)
    df_full["dispatch_time"] = df_full["dispatch_time"].clip(lower=5, upper=600)

    # More varied phone_time using gamma
    df_full["phone_time"] = np.concatenate(
        [
            np.random.exponential(scale=80, size=int(len(df_full) * 0.8)),  # Fast calls
            np.random.gamma(
                shape=2, scale=200, size=int(len(df_full) * 0.2)
            ),  # Slower calls
        ]
    ).astype(int)

    # ack_time describes the time from the first dispatch to the time the unit marks enroute
    shape, scale = 2.0, 30.0
    df_full["ack_time"] = np.random.gamma(shape, scale, size=len(df_full)).astype(int)
    df_full["ack_time"] = df_full["ack_time"].clip(lower=2, upper=40)

    # More varied enroute_time using gamma with different parameters
    shape, scale = 6.0, 70.0
    df_full["enroute_time"] = np.random.gamma(shape, scale, size=len(df_full)).astype(
        int
    )
    df_full["enroute_time"] = df_full["enroute_time"].clip(lower=300, upper=900)

    # More varied on_scene_time using gamma with heavy tail
    shape, scale = 3.0, 800.0
    df_full["on_scene_time"] = np.random.gamma(shape, scale, size=len(df_full)).astype(
        int
    )
    df_full["on_scene_time"] = df_full["on_scene_time"].clip(lower=300, upper=7200)

    # Add process_time column - sum of queue_time and dispatch_time
    df_full["process_time"] = df_full["queue_time"] + df_full["dispatch_time"]

    df_full["total_time"] = (
        df_full["queue_time"]
        + df_full["dispatch_time"]
        + df_full["ack_time"]
        + df_full["enroute_time"]
        + df_full["on_scene_time"]
    )

    # Time stamp for when call was sent to dispatch queue
    df_full["time_call_queued"] = df_full["event_time"] + pd.to_timedelta(
        df_full["queue_time"], unit="s"
    )

    # Time stamp for when call was dispatched to a unit
    df_full["time_call_dispatched"] = df_full["time_call_queued"] + pd.to_timedelta(
        df_full["dispatch_time"], unit="s"
    )

    # Time stamp for when unit acknowledged the call
    df_full["time_call_acknowledged"] = df_full[
        "time_call_dispatched"
    ] + pd.to_timedelta(df_full["ack_time"], unit="s")

    # Time stamp for when phone call was disconnected
    df_full["time_call_disconnected"] = df_full["event_time"] + pd.to_timedelta(
        df_full["phone_time"], unit="s"
    )

    # Time stamp for when unit arrived on scene
    df_full["time_unit_enroute"] = df_full["time_call_acknowledged"] + pd.to_timedelta(
        df_full["enroute_time"], unit="s"
    )

    # Time stamp for close of call
    df_full["time_call_closed"] = df_full["event_time"] + pd.to_timedelta(
        df_full["total_time"], unit="s"
    )

    law_dispositions = DISPOSITIONS
    nonlaw_dispositions = [d for d in DISPOSITIONS if d != "ARREST MADE"]

    def assign_disposition(agency):
        if agency == "LAW":
            return fake.disposition()
        else:
            return random.choice(nonlaw_dispositions)

    # Add disposition column with random dispositions
    df_full["disposition"] = df_full["agency"].apply(assign_disposition)

    # List all your datetime columns
    datetime_cols = [
        "event_time",
        "time_call_queued",
        "time_call_dispatched",
        "time_call_acknowledged",
        "time_call_disconnected",
        "time_unit_enroute",
        "time_call_closed",
    ]

    # Format each datetime column as 'YYYY-MM-DD HH:mm:ss'
    for col in datetime_cols:
        df_full[col] = df_full[col].dt.strftime("%Y-%m-%d %H:%M:%S")
        

    return df_full, call_taker_names, dispatcher_names

class DateValidator(Validator):
    def validate(self, document):
        try:
            datetime.strptime(document.text, '%Y-%m-%d')
        except ValueError:
            raise ValidationError(
                message='Please enter a valid date in YYYY-MM-DD format',
                cursor_position=len(document.text)
            )

def main():
    """
    This is the main entry point of the script. It provides an interactive command line interface
    to generate 911 dispatch data and saves it to a CSV file.
    """

    if PYINQUIRER_AVAILABLE:
        # Interactive mode with PyInquirer
        questions = [
            {
                'type': 'input',
                'name': 'num_records',
                'message': 'How many records would you like to generate?',
                'default': '10000',
                'validate': lambda val: val.isdigit() and int(val) > 0 or 'Please enter a positive number'
            },
            {
                'type': 'input',
                'name': 'start_date',
                'message': 'Enter start date (YYYY-MM-DD):',
                'default': '2024-01-01',
                'validate': DateValidator
            },
            {
                'type': 'input',
                'name': 'end_date',
                'message': 'Enter end date (YYYY-MM-DD):',
                'default': '2024-12-31',
                'validate': DateValidator
            },
            {
                'type': 'input',
                'name': 'num_names',
                'message': 'How many names would you like to generate per shift?',
                'default': '8',
                'validate': lambda val: val.isdigit() and int(val) > 0 or 'Please enter a positive number'
            },
            {
                'type': 'input',
                'name': 'locale',
                'message': 'Enter the Faker locale (e.g., en_US, en_GB, fr_FR, de_DE):',
                'default': DEFAULT_LOCALE
            },
            {
                'type': 'input',
                'name': 'output_file',
                'message': 'Enter the output file path:',
                'default': 'computer_aided_dispatch.csv'
            },
            {
                'type': 'input',
                'name': 'selected_agencies',
                'message': 'Enter agencies to include (comma-separated, e.g., LAW,FIRE):',
                'default': ''
            },
            {
                'type': 'input',
                'name': 'agency_probabilities',
                'message': 'Enter agency probabilities (comma-separated, e.g., 0.7,0.2,0.1):',
                'default': '',
            },
        ]

        answers = prompt(questions)

        num_records = int(answers['num_records'])
        start_date = answers['start_date']
        end_date = answers['end_date']
        num_names = int(answers['num_names'])
        locale = answers['locale']
        output_file = answers['output_file']
        selected_agencies = answers['selected_agencies'].split(',') if answers['selected_agencies'] else None
        agency_probabilities = None
        if answers.get('agency_probabilities'):
            try:
                agency_probabilities = [float(x) for x in answers['agency_probabilities'].split(',')]
            except Exception:
                print("Invalid agency probabilities format. Must be comma-separated floats.")
                sys.exit(1)
    else:
        # Command-line argument mode
        parser = argparse.ArgumentParser(description="Generate synthetic 911 dispatch data")
        parser.add_argument('-n', '--num-records', type=int, default=10000,
                            help='Number of records to generate (default: 10000)')
        parser.add_argument('-s', '--start-date', type=str, default='2024-01-01',
                            help='Start date in YYYY-MM-DD format (default: 2024-01-01)')
        parser.add_argument('-e', '--end-date', type=str, default='2024-12-31',
                            help='End date in YYYY-MM-DD format (default: 2024-12-31)')
        parser.add_argument('--num-names', type=int, default=8,
                            help='Number of names to generate per shift (default: 8)')
        parser.add_argument('-l', '--locale', type=str, default=DEFAULT_LOCALE,
                            help=f'Faker locale for generating localized data (default: {DEFAULT_LOCALE})')
        parser.add_argument('-o', '--output-file', type=str, default='computer_aided_dispatch.csv',
                            help='Output file path (default: computer_aided_dispatch.csv)')
        parser.add_argument('-a', '--agencies', type=str, default='',
                            help='Comma-separated list of agencies to include (e.g., LAW,FIRE)')
        parser.add_argument('--agency-probabilities', type=str, default='',
                            help='Comma-separated probabilities for selected agencies (e.g., 0.7,0.2,0.1)')

        args = parser.parse_args()

        # Validate dates
        try:
            datetime.strptime(args.start_date, '%Y-%m-%d')
            datetime.strptime(args.end_date, '%Y-%m-%d')
        except ValueError:
            print("Error: Dates must be in YYYY-MM-DD format")
            sys.exit(1)

        num_records = args.num_records
        start_date = args.start_date
        end_date = args.end_date
        num_names = args.num_names
        locale = args.locale
        output_file = args.output_file
        selected_agencies = args.agencies.split(',') if args.agencies else None
        agency_probabilities = None
        if args.agency_probabilities:
            try:
                agency_probabilities = [float(x) for x in args.agency_probabilities.split(',')]
            except Exception:
                print("Invalid agency probabilities format. Must be comma-separated floats.")
                sys.exit(1)

    # Generate data with specified parameters
    df_full, call_taker_names, dispatcher_names = generate_911_data(
        num_records=num_records,
        start_date=start_date,
        end_date=end_date,
        num_names=num_names,
        locale=locale,
        selected_agencies=selected_agencies,
        agency_probabilities=agency_probabilities
    )

    # Save the DataFrame to a CSV file
    df_full.to_csv(output_file, index=False)

    print(f"\nCSV file saved to {output_file}")
    print(f"Total records generated: {len(df_full)}")

    # Quick summary statistics of the new columns
    print("\nSummary Statistics for New Columns:")
    print(df_full[["phone_time", "process_time", "total_time"]].describe())

    print("\nCall Taker Names per Shift:")
    for shift, names in call_taker_names.items():
        print(f"Shift {shift}: {names}")

    print("\nDispatcher Names per Shift:")
    for shift, names in dispatcher_names.items():
        print(f"Shift {shift}: {names}")

if __name__ == "__main__":
    main()
