#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: A pointer to a pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	int count = 0;
	listint_t *p1 = *head;
	listint_t *p2 = *head;
	listint_t *temp = NULL;

	if (*head == NULL || (*head)->next == NULL)
        	return (1);

	while (p1 != NULL)
	{
		count++;
		p1 = p1->next;
	}
	p1 = *head;

	while (p2 != temp)
	{
		if (temp == p2->next && count % 2 != 0)
			return (1);

		while (p1->next->next != temp)
			p1 = p1->next;
		temp = p1->next;

		if (p2->n == temp->n)
		{
			p2 = p2->next;
			p1 = p2;
		}
		else
		{
			return (0);
		}
	}
	return (1);
}
