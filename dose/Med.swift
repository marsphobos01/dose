//
//  Med.swift
//  Dose
//
//  Created by Morgan Bennett on 26/07/2026.
//
import SwiftData
import Foundation

@Model
class Med {
    var name: String
    var dosage: Int
    var unit: String = "mg"
    var dailyAmount: Int
    var totalAmount: Int
    var startDate: Date?
    var expirationDate: Date?
    var notes: String?
    var timeTaken: Date?
    var hasTakenToday: Bool {
        if timeTaken == nil {
            return false
        } else {
            return Calendar.current.isDateInToday(timeTaken!)
        }
    }
    var canTake: Bool {
        return !hasTakenToday
    }
    var isExpiringSoon: Bool {
        if expirationDate == nil {
            return false
        } else if expirationDate! <= Calendar.current.date(byAdding: .day, value: 7, to: Date())! {
            return true
        } else {
            return false
        }
    }
    
    init(name: String, dosage: Int, unit: String, dailyAmount: Int, totalAmount: Int, startDate: Date?, expirationDate: Date?, notes: String?) {
        self.name = name
        self.dosage = dosage
        self.unit = unit
        self.dailyAmount = dailyAmount
        self.totalAmount = totalAmount
        self.startDate = startDate
        self.expirationDate = expirationDate
        self.notes = notes
    }
    
    func markTaken() {
        if self.canTake == true {
            self.timeTaken = Date()
            self.totalAmount = max(self.totalAmount - self.dailyAmount,0)
        }
    }
}


