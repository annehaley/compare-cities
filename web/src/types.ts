export interface State {
    name: string,
    abbreviation: string,
}

export interface City {
    average_wages_and_salaries: number,
    county_fips: number,
    county_name: string,
    density: number,
    id: string,
    incorporated: boolean,
    latitude: number,
    longitude: number,
    military: boolean,
    name: string,
    per_capita_dividends_interest_and_rent: number,
    per_capita_net_earnings: number,
    per_capita_personal_income: number,
    population: number,
    ranking: number,
    state_id: string,
    timezone: string,
    total_employment: number,
    zips: string,
}

export interface Marker {
    id: string,
    position: {
        lat: number,
        lng: number,
    }
}
