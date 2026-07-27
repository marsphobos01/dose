//
//  MedFormView.swift
//  Dose
//
//  Created by Morgan Bennett on 26/07/2026.
//

import SwiftUI

struct MedFormView: View {
    @State private var name: String = ""
    @State private var dosage: Int = 0
    @State private var unit: String = "mg"
    @State private var dailyAmount: Int = 0
    @State private var totalAmount: Int = 0
    @State private var hasStartDate: Bool = false
    @State private var startDate: Date = Date()
    @State private var hasExpirationDate: Bool = false
    @State private var expirationDate: Date = Date()
    
    var body: some View {
        TextField("Name", text: $name)
        TextField("Dosage", value: $dosage, format: .number)
        TextField("Unit", text: $unit)
        TextField("Daily Amount",value: $dailyAmount, format: .number)
        TextField("Total Amount",value: $totalAmount, format: .number)
        Toggle("Has start date", isOn: $hasStartDate)
        if hasStartDate {
            DatePicker("Start Date", selection: $startDate, displayedComponents: .date)
        }
        Toggle("Has expiration date", isOn: $hasExpirationDate)
        if hasExpirationDate {
            DatePicker("Expiration Date", selection: $expirationDate, displayedComponents: .date)
        }
        
    }
}

#Preview {
    MedFormView()
}
