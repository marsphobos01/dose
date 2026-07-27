//
//  MedListView.swift
//  Dose
//
//  Created by Morgan Bennett on 26/07/2026.
//

import SwiftUI
import SwiftData

struct MedListView: View {
    @Query var meds: [Med]
    @State private var showingAddForm = false
    var body: some View {
        Button("Add Med") { showingAddForm = true }
        List(meds) { med in Text(med.name)}
            .sheet(isPresented: $showingAddForm) { MedFormView() }
    }
}

#Preview {
    MedListView()
}
