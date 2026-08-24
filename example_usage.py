from client import SustainableAlgaePlantPetNutritionCalculatorClient

def main():
    client = SustainableAlgaePlantPetNutritionCalculatorClient()
    res = client.formulate_sustainable_canine_diet(20.0, 'sensitive_skin_and_gut')
    print('Diet Plan: ' + res['diet_plan_id'] + ' (' + res['hypoallergenic_certification'] + ')')
    print('Carbon Cut: -' + str(res['carbon_footprint_reduction_vs_beef_pct']) + '% | Water Saved: ' + str(res['annual_water_saved_liters']) + ' L/yr')
    print('Proteins: ' + ', '.join(res['base_protein_sources']))

if __name__ == '__main__':
    main()
