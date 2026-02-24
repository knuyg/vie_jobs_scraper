use serde::{Deserialize, Serialize};
use reqwest::Client;

// API Request Body
#[derive(Serialize)]
struct SearchRequest {
    limit: u32,
    skip: u32,
    sort: Vec<String>,
    activity_sector_id: Vec<u32>,
    missions_types_ids: Vec<u32>,
    missions_durations: Vec<u32>,
    geographic_zones: Vec<u32>,
    countries_ids: Vec<u32>,
    studies_level_id: Vec<u32>,
    companies_sizes: Vec<u32>,
    specializations_ids: Vec<u32>,
    entreprises_ids: Vec<u32>,
    mission_start_date: Option<String>,
    query: Option<String>,
}

// API Response Structure
#[derive(Deserialize, Debug)]
#[serde(rename_all = "camelCase")]
struct VieJob {
    id: u32,
    mission_title: String,
    organization_name: String,
    city_name: String,
    country_name_en: String,
    mission_type: String,
    mission_duration: u32,
    indemnite: Option<f64>,
    mission_start_date: Option<String>,
    reference: String,
    teleworking_available: bool,
    contact_email: String,
}

#[derive(Deserialize)]
struct ApiResponse {
    result: Vec<VieJob>,
    count: u32,
}

// function that fetches one page of results from the API
// async because we will run this function several times at the same time
async fn fetch_jobs(client: &Client, skip: u32) -> Result<ApiResponse, reqwest::Error>{
    let request_body = SearchRequest {
        limit: 100,
        skip,
        sort: vec![String::from("0")],
        activity_sector_id: vec![],
        missions_types_ids: vec![],
        missions_durations: vec![],
        geographic_zones: vec![],
        countries_ids: vec![],
        studies_level_id: vec![],
        companies_sizes: vec![],
        specializations_ids: vec![],
        entreprises_ids: vec![0],
        mission_start_date: None,
        query: None,
    };

    let response = client
    .post("https://civiweb-api-prd.azurewebsites.net/api/Offers/search")
    .json(&request_body)   // serialize our struct to JSON automatically
    .send()                // send the request -- this is where we await the network
    .await?                // ? means: if this fails, return the error immediately
    .json::<ApiResponse>() // deserialize the response JSON into our ApiResponse struct
    .await?;               // again, ? for error propagation

    Ok(response)

}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = Client::new();

    // Test with just the first page
    let response = fetch_jobs(&client, 0).await?;

    println!("Total jobs available: {}", response.count);
    println!("Jobs fetched this page: {}", response.result.len());
    println!("First job: {:#?}", response.result[0]);

    Ok(())
}
